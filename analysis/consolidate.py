"""把 Bloomberg 匯出的兩份 Excel 與 Fed 的 TP 資料統整成一份日資料。

輸入（預設放在 data/private/raw/，不納入版控）：
    bbg_template.xlsx                 MoveRates 專案的 BBG 範本（每個 ticker 一組「日期／數值」兩欄，已貼成值）
    us_bond_vol_rv_iv_refreshed.xlsx  本 repo 的 Excel 範本在 Bloomberg 重新整理後存檔的版本
    data/THREEFYTP10.csv              Kim-Wright 10Y TP（FRED）
    data/DKW_updates.csv              DKW 拆解（Fed staff）

輸出：
    data/private/market_daily.csv     日資料（寬表），只到最後一個完整收盤日（--asof，預設自動判斷）
    data/private/market_daily.xlsx    同上，另附「說明」分頁（欄位、單位、來源、筆數）

用法：
    python analysis/consolidate.py [--template PATH] [--workbook PATH] [--asof YYYY-MM-DD]

注意：
    * Bloomberg 資料受授權限制，repo 是公開的，所以輸出放在 data/private/（已列入 .gitignore）。
    * 範本的 MOVE BDH 雖然指定 Days=W，Bloomberg 仍回傳每一個日曆日（含週末），且隱藏日期，
      所以和其他欄位錯位。這裡依「起始日起算的日曆日」重建 MOVE 的日期，並用 bbg_template
      附日期的 MOVE 驗證兩者一致後才採用。
"""

import argparse
import csv
import datetime as dt
from pathlib import Path

import openpyxl
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "private" / "raw"
OUT = ROOT / "data" / "private" / "market_daily.csv"

# bbg_template 欄位名 → (輸出欄名, 換算係數)
TEMPLATE_MAP = {
    "UST3M": ("UST3M", 1.0),
    "UST2Y": ("UST2Y", 1.0),
    "UST5Y": ("UST5Y", 1.0),
    "UST10Y": ("UST10Y", 1.0),
    "UST30Y": ("UST30Y", 1.0),
    "MOVE": ("MOVE", 1.0),
    "HY_OAS": ("HY_OAS_bp", 100.0),   # 範本中為 %，換成 bp
    "IG_OAS": ("IG_OAS_bp", 100.0),
    "CDX_IG": ("CDX_IG_bp", 1.0),
    "CDX_HY": ("CDX_HY_bp", 1.0),
}
DKW_MAP = {
    "exp.real.short.rate.10": "DKW_ERSR10_bp",
    "real.term.prem.10": "DKW_RTP10_bp",
    "exp.inflation.10": "DKW_EINF10_bp",
    "inflation.risk.prem.10": "DKW_IRP10_bp",
    "tips.liq.prem.10": "DKW_LIQ10_bp",
    "nominal.yield.fitted.10": "DKW_NOM10_bp",
}
DICTIONARY = {
    "UST3M": ("3M 公債殖利率", "%", "bbg_template：USGG3M Index"),
    "UST2Y": ("2Y 公債殖利率", "%", "bbg_template：USGG2YR Index"),
    "UST5Y": ("5Y 公債殖利率", "%", "bbg_template：USGG5YR Index"),
    "UST10Y": ("10Y 公債殖利率", "%", "Excel 範本：USGG10YR Index（2024 起）；之前為 bbg_template"),
    "UST30Y": ("30Y 公債殖利率", "%", "bbg_template：USGG30YR Index"),
    "SOFR10Y": ("10Y SOFR OIS swap", "%", "Excel 範本：USOSFR10 Curncy"),
    "TIPS10Y": ("10Y TIPS 實質殖利率", "%", "Excel 範本：USGGT10Y Index"),
    "BEI10Y": ("10Y Breakeven Inflation", "%", "Excel 範本：USGGBE10 Index"),
    "MOVE": ("ICE BofA MOVE Index（1M）", "bp", "bbg_template：MOVE Index；10/2 由 Excel 範本依日曆日校正後補上"),
    "HY_OAS_bp": ("HY 利差 OAS", "bp", "bbg_template：LF98OAS Index（原為 %，×100）"),
    "IG_OAS_bp": ("IG 利差 OAS", "bp", "bbg_template：LUACOAS Index（原為 %，×100）"),
    "CDX_IG_bp": ("CDX IG 5Y", "bp", "bbg_template：IBOXUMAE CBBT Curncy"),
    "CDX_HY_bp": ("CDX HY 5Y", "bp", "bbg_template：IBOXHYSE CBBT Curncy"),
    "KW_TP10_bp": ("Kim-Wright 10Y TP", "bp", "FRED THREEFYTP10（data/THREEFYTP10.csv）"),
    "DKW_ERSR10_bp": ("DKW 10Y 預期實質短率", "bp", "Fed staff DKW_updates.csv"),
    "DKW_RTP10_bp": ("DKW 10Y 實質 TP", "bp", "Fed staff DKW_updates.csv"),
    "DKW_EINF10_bp": ("DKW 10Y 預期通膨", "bp", "Fed staff DKW_updates.csv"),
    "DKW_IRP10_bp": ("DKW 10Y 通膨風險溢酬", "bp", "Fed staff DKW_updates.csv"),
    "DKW_LIQ10_bp": ("DKW 10Y TIPS 流動性溢酬", "bp", "Fed staff DKW_updates.csv"),
    "DKW_NOM10_bp": ("DKW 10Y 名目殖利率（fitted）", "bp", "Fed staff DKW_updates.csv"),
}
COLUMNS = ["UST3M", "UST2Y", "UST5Y", "UST10Y", "UST30Y", "SOFR10Y", "TIPS10Y", "BEI10Y", "MOVE",
           "HY_OAS_bp", "IG_OAS_bp", "CDX_IG_bp", "CDX_HY_bp", "KW_TP10_bp"] + list(DKW_MAP.values())


def is_date(v):
    return isinstance(v, (dt.datetime, dt.date))


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def read_template(path):
    ws = openpyxl.load_workbook(path, data_only=True)["data"]
    out = {}
    for j in range(1, ws.max_column + 1, 2):
        name = ws.cell(1, j).value
        if name not in TEMPLATE_MAP:
            continue
        rows = {}
        for i in range(2, ws.max_row + 1):
            d, v = ws.cell(i, j).value, ws.cell(i, j + 1).value
            if is_date(d) and is_num(v):
                rows[pd.Timestamp(d)] = float(v)
        if rows:
            col, k = TEMPLATE_MAP[name]
            out[col] = pd.Series(rows).sort_index() * k
    return out


def read_workbook(path):
    wb = openpyxl.load_workbook(path, data_only=True)
    st, ws = wb["Settings"], wb["BBG_Data"]
    start, end = pd.Timestamp(st["B3"].value), pd.Timestamp(st["B4"].value)

    def column(j):
        vals = []
        for i in range(2, ws.max_row + 1):
            v = ws.cell(i, j).value
            if v is None or v == "":
                break
            vals.append(v)
        return vals

    dates = pd.to_datetime(column(1))
    n = len(dates)
    out = {}
    for j, name in ((2, "UST10Y"), (3, "SOFR10Y"), (6, "TIPS10Y"), (7, "BEI10Y")):
        vals = column(j)
        if len(vals) != n:
            raise ValueError(f"{name} 長度 {len(vals)} 與日期 {n} 不一致，請檢查 BBG_Data")
        out[name] = pd.Series([float(v) if is_num(v) else float("nan") for v in vals], index=dates)

    move = column(4)
    cal_days = (end - start).days + 1
    if len(move) == n:
        out["MOVE"] = pd.Series([float(v) for v in move], index=dates)
        layout = "aligned"
    elif len(move) == cal_days:
        idx = pd.date_range(start, periods=cal_days, freq="D")
        s = pd.Series([float(v) for v in move], index=idx)
        out["MOVE"] = s[s.index.weekday < 5]
        layout = "calendar-day"
    else:
        raise ValueError(f"MOVE 長度 {len(move)} 無法判斷日期（交易日 {n}、日曆日 {cal_days}）")
    return out, layout, start, end


def read_kw(path):
    s = {}
    with open(path, newline="") as f:
        for rec in csv.DictReader(f):
            v = rec["THREEFYTP10"].strip()
            if v and v != ".":
                s[pd.Timestamp(rec["observation_date"])] = float(v) * 100
    return pd.Series(s).sort_index()


def read_dkw(path):
    lines = Path(path).read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith('"date"'))
    df = pd.read_csv(path, skiprows=start, na_values="NA", parse_dates=["date"]).set_index("date")
    return {new: df[old] * 100 for old, new in DKW_MAP.items()}


def last_published(s):
    """最後一個「數值有變動」的日期，用來排除 Fill=P 往後補的日子。"""
    changed = s.ne(s.shift())
    return s.index[changed][-1]


def write_xlsx(df, asof, checks, layout):
    """同一份資料另存 Excel（含欄位說明），方便直接檢視。"""
    from openpyxl.styles import Alignment, Font, PatternFill

    path = OUT.with_suffix(".xlsx")
    with pd.ExcelWriter(path, engine="openpyxl") as xw:
        info = [["欄位", "內容", "單位", "來源", "筆數", "起", "迄"]]
        for col in df.columns:
            s = df[col].dropna()
            name, unit, src = DICTIONARY[col]
            info.append([col, name, unit, src, len(s), s.index.min().date(), s.index.max().date()])
        notes = [
            [],
            ["截止日", str(asof.date()), "最後一個完整收盤日；10/5 的盤中／補值資料不列入"],
            ["MOVE 校正", layout, "Excel 範本的 MOVE BDH 回傳每個日曆日，已依日期重建並與 bbg_template 比對"],
        ] + [[f"驗證 {n}", f"重疊 {k} 天", f"最大差 {d:.1e}"] for n, k, d in checks] + [
            ["快照日", "", "bbg_template 最後一天為盤中快照，已捨棄"],
            ["授權", "", "Bloomberg 資料僅供內部使用，勿上傳公開 repo"],
        ]
        pd.DataFrame(info[1:] + notes, columns=info[0]).to_excel(xw, sheet_name="說明", index=False)
        out = df.copy()
        out.index = out.index.date
        out.index.name = "date"
        out.to_excel(xw, sheet_name="daily")
        for ws in xw.book.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    c.font = Font(name="Arial", size=10, bold=c.row == 1)
            for c in ws[1]:
                c.fill = PatternFill("solid", fgColor="1F3864")
                c.font = Font(name="Arial", size=10, bold=True, color="FFFFFF")
                c.alignment = Alignment(wrap_text=True, vertical="center")
        sh = xw.book["說明"]
        for col, w in zip("ABCDEFG", (14, 30, 8, 60, 8, 12, 12)):
            sh.column_dimensions[col].width = w
        for row in sh.iter_rows(min_row=2, min_col=6, max_col=7):
            for c in row:
                c.number_format = "yyyy-mm-dd"
        dl = xw.book["daily"]
        dl.column_dimensions["A"].width = 12
        dl.freeze_panes = "B2"
        for row in dl.iter_rows(min_row=2, max_col=1):
            row[0].number_format = "yyyy-mm-dd"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", default=RAW / "bbg_template.xlsx")
    ap.add_argument("--workbook", default=RAW / "us_bond_vol_rv_iv_refreshed.xlsx")
    ap.add_argument("--asof", default=None, help="最後一個完整收盤日；預設取 MOVE 最後一次更新的日期")
    args = ap.parse_args()

    tpl = read_template(args.template)
    wbk, layout, wb_start, wb_end = read_workbook(args.workbook)
    # 範本最後一天是盤中快照（例：10Y 快照 5.2495%，收盤 5.2706%），一律捨棄；收盤值由較晚抓取的 Excel 補上
    snap = max(s.index.max() for s in tpl.values())
    tpl = {k: v[v.index < snap] for k, v in tpl.items()}

    # 驗證：兩份檔案重疊期間的 MOVE 與 10Y 必須一致
    checks = []
    for name in ("MOVE", "UST10Y"):
        a, b = tpl[name], wbk[name]
        common = a.index.intersection(b.index)
        diff = (a[common] - b[common]).abs().max()
        checks.append((name, len(common), diff))
        if diff > 1e-6:
            raise ValueError(f"{name} 兩份資料重疊期間不一致（最大差 {diff}），請先檢查")

    asof = pd.Timestamp(args.asof) if args.asof else last_published(wbk["MOVE"])

    series = {}
    for col in COLUMNS:
        parts = []
        if col in wbk:
            parts.append(wbk[col])     # 重新整理過的 Excel 較晚抓取，收盤值優先
        if col in tpl:
            parts.append(tpl[col])
        if parts:
            s = parts[0]
            for p in parts[1:]:
                s = s.combine_first(p)
            series[col] = s
    series["KW_TP10_bp"] = read_kw(ROOT / "data" / "THREEFYTP10.csv")
    series.update(read_dkw(ROOT / "data" / "DKW_updates.csv"))

    market_cols = [c for c in COLUMNS if not c.startswith(("KW_", "DKW_"))]
    idx = sorted(set().union(*[series[c].index for c in market_cols if c in series]))
    idx = pd.DatetimeIndex([d for d in idx if d.weekday() < 5 and d <= asof])
    df = pd.DataFrame(index=idx)
    for col in COLUMNS:
        if col in series:
            df[col] = series[col].reindex(idx)
    df.index.name = "date"

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, float_format="%.6g")
    write_xlsx(df, asof, checks, layout)

    print(f"MOVE 版面：{layout}（範本起始 {wb_start.date()}、結束 {wb_end.date()}）")
    print(f"捨棄 bbg_template 快照日 {snap.date()} 的數值")
    for name, n, diff in checks:
        print(f"驗證 {name}：重疊 {n} 天，最大差 {diff:.2e}")
    print(f"截止日（as-of）：{asof.date()}；輸出 {OUT.relative_to(ROOT)}，{len(df)} 列")
    for col in df.columns:
        s = df[col].dropna()
        print(f"  {col:15s} {len(s):5d} 筆  {s.index.min().date()} → {s.index.max().date()}")


if __name__ == "__main__":
    main()
