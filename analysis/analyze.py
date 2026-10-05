"""讀取 data/private/market_daily.csv，算出筆記與簡報用的統計。

輸出（皆在 data/private/analysis/，不納入版控）：
    summary.json      所有表格數字（筆記、簡報由此取數）
    weekly_2026.csv   2026 年每週五的 MOVE、10Y RV、10Y、HY OAS（簡報圖表用）

定義：
    每日變動      (今日 − 前一日) × 100，單位 bp；變動恰為 0 視為休市補值，不計入 RV
    RV            最近 21 個每日變動的樣本標準差 × √252（年化 normal vol，bp/y），至少 18 筆
    IV − RV       MOVE − 10Y 21 日 RV（MOVE 為 1 個月期，與 21 個交易日對應）
    事後 VRP      當日 MOVE − 之後 21 個交易日實際發生的 10Y RV
    加權 RV       2Y/5Y/10Y/30Y 的 RV 以 20/20/40/20% 加權，對應 MOVE 的期限權重
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "private" / "market_daily.csv"
OUT = ROOT / "data" / "private" / "analysis"

WIN, MINP, ANN = 21, 18, 252
HIST = ("2017-01-01", "2025-12-31")
CREDIT = ["HY_OAS_bp", "IG_OAS_bp", "CDX_IG_bp", "CDX_HY_bp"]
TENORS = ["UST3M", "UST2Y", "UST5Y", "UST10Y", "UST30Y"]


def r(x, nd=1):
    return None if x is None or pd.isna(x) else round(float(x), nd)


def main():
    df = pd.read_csv(SRC, parse_dates=["date"], index_col="date")
    asof = df.index.max()

    def lvl(col, d):
        s = df[col].dropna()[: pd.Timestamp(d)]
        return s.iloc[-1]

    def chg_bp(col, a, b):  # 殖利率類：% → bp
        return (lvl(col, b) - lvl(col, a)) * 100

    def chg(col, a, b):     # 已是 bp 或指數點
        return lvl(col, b) - lvl(col, a)

    # ---- RV 與 IV − RV
    d = (df[["UST2Y", "UST5Y", "UST10Y", "UST30Y"]].diff() * 100)
    d = d.mask(d == 0)
    rv = d.rolling(WIN, min_periods=MINP).std() * np.sqrt(ANN)
    rv10 = rv["UST10Y"]
    rvw = 0.2 * rv["UST2Y"] + 0.2 * rv["UST5Y"] + 0.4 * rv["UST10Y"] + 0.2 * rv["UST30Y"]
    fwd10 = d["UST10Y"][::-1].rolling(WIN, min_periods=MINP).std()[::-1].shift(-1) * np.sqrt(ANN)
    move = df["MOVE"]
    ivrv = (move - rv10).dropna()
    hist_ivrv = ivrv[HIST[0]:HIST[1]]
    hist_move = move[HIST[0]:HIST[1]].dropna()

    periods = [
        ("開戰前（1/1–2/27）", "2026-01-01", "2026-02-27"),
        ("開戰衝擊（3–4 月）", "2026-03-01", "2026-04-30"),
        ("預期主導（5–8 月）", "2026-05-01", "2026-08-31"),
        ("9 月第一階段（9/1–9/22）", "2026-09-01", "2026-09-22"),
        ("9 月第二階段（9/23–10/2）", "2026-09-23", "2026-10-02"),
        ("2017–2025 平均", HIST[0], HIST[1]),
    ]
    vol_table = []
    for name, a, b in periods:
        vol_table.append({
            "period": name,
            "MOVE": r(move[a:b].mean()),
            "RV10": r(rv10[a:b].mean()),
            "RVW": r(rvw[a:b].mean()),
            "IV_RV": r((move - rv10)[a:b].mean()),
            "VRP_ex": r((move - fwd10)[a:b].mean()),
            "mean_abs_daily_10Y": r(d["UST10Y"][a:b].abs().mean(), 2),
        })

    def ivrv_at(day):
        x = ivrv[: pd.Timestamp(day)].iloc[-1]
        return {"date": str(ivrv[: pd.Timestamp(day)].index[-1].date()),
                "MOVE": r(move[: pd.Timestamp(day)].dropna().iloc[-1]),
                "RV10": r(rv10[: pd.Timestamp(day)].dropna().iloc[-1]),
                "IV_RV": r(x), "pctile": r((hist_ivrv < x).mean() * 100, 0)}

    ivrv_points = {k: ivrv_at(v) for k, v in
                   [("2025-04-08", "2025-04-08"), ("2026-03-26", "2026-03-26"), ("2026-09-22", "2026-09-22"),
                    ("2026-09-30", "2026-09-30"), ("asof", asof)]}
    mj = (move - rv10)["2026-05-01":"2026-08-31"].dropna()
    may_aug = {"min": r(mj.min()), "min_day": str(mj.idxmin().date()), "days_below_-5": int((mj < -5).sum()),
               "days": int(len(mj)), "mean_0520_0710": r(mj["2026-05-20":"2026-07-10"].mean())}
    m0, m1 = move[:pd.Timestamp("2026-09-22")].iloc[-1], move[:asof].dropna().iloc[-1]
    v0, v1 = rv10[:pd.Timestamp("2026-09-22")].iloc[-1], rv10[:asof].dropna().iloc[-1]
    move_jump = {"MOVE_chg": r(m1 - m0), "RV_chg": r(v1 - v0), "IVRV_chg": r((m1 - v1) - (m0 - v0)),
                 "RV_share": r((v1 - v0) / (m1 - m0) * 100, 0)}
    recent = d["UST10Y"]["2026-09-23":asof].dropna()
    rv_since_0923 = recent.std() * np.sqrt(ANN)

    # ---- 原文數字核對
    y = df["UST10Y"].dropna()
    war_low_day = y["2026-02":"2026-03"].idxmin()
    verify = {
        "ust10_close_0930": r(lvl("UST10Y", "2026-09-30"), 4),
        "ust10_close_1001": r(lvl("UST10Y", "2026-10-01"), 4),
        "ust10_close_asof": r(lvl("UST10Y", asof), 4),
        "ust10_2026_max_close": r(y["2026"].max(), 4), "ust10_2026_max_day": str(y["2026"].idxmax().date()),
        "war_low_day": str(war_low_day.date()), "war_low": r(y[war_low_day], 4),
        "since_war_low_to_0930_bp": r(chg_bp("UST10Y", war_low_day, "2026-09-30")),
        "sep_change_bp": r(chg_bp("UST10Y", "2026-08-31", "2026-09-30")),
        "apr30": r(lvl("UST10Y", "2026-04-30"), 4),
        "tips_since_war_low_bp": r(chg_bp("TIPS10Y", war_low_day, "2026-09-30")),
        "bei_since_war_low_bp": r(chg_bp("BEI10Y", war_low_day, "2026-09-30")),
        "move_0930": r(lvl("MOVE", "2026-09-30")), "move_1001": r(lvl("MOVE", "2026-10-01")),
        "move_mar_peak": r(move["2026-03"].max()), "move_mar_peak_day": str(move["2026-03"].idxmax().date()),
        "move_apr2025_peak": r(move["2025-04"].max()), "move_apr2025_peak_day": str(move["2025-04"].idxmax().date()),
        "move_may_aug_mean": r(move["2026-05":"2026-08"].mean()),
        "move_may_aug_min": r(move["2026-05":"2026-08"].min()), "move_may_aug_max": r(move["2026-05":"2026-08"].max()),
        "move_may_aug_mean_pctile": r((hist_move < move["2026-05":"2026-08"].mean()).mean() * 100, 0),
        "move_hist_mean": r(hist_move.mean()),
        "bei_0915": r(lvl("BEI10Y", "2026-09-15"), 4), "bei_0917": r(lvl("BEI10Y", "2026-09-17"), 4),
        "bei_asof": r(lvl("BEI10Y", asof), 4),
        "kw_0831": r(lvl("KW_TP10_bp", "2026-08-31")), "kw_0922": r(lvl("KW_TP10_bp", "2026-09-22")),
        "kw_last": r(df["KW_TP10_bp"].dropna().iloc[-1]), "kw_last_day": str(df["KW_TP10_bp"].dropna().index[-1].date()),
    }

    # ---- 市場口徑拆解：10Y = TIPS + BEI
    decomp = []
    for name, a, b in [("今年以來", "2025-12-31", asof), ("開戰低點以來", war_low_day, "2026-09-30"),
                       ("6/30 → 8/31", "2026-06-30", "2026-08-31"), ("9 月", "2026-08-31", "2026-09-30"),
                       ("升息後（9/15 → 10/2）", "2026-09-15", asof)]:
        n, t, e = chg_bp("UST10Y", a, b), chg_bp("TIPS10Y", a, b), chg_bp("BEI10Y", a, b)
        decomp.append({"period": name, "start": str(pd.Timestamp(a).date()), "end": str(pd.Timestamp(b).date()),
                       "UST10Y": r(n), "TIPS10Y": r(t), "BEI10Y": r(e), "real_share": r(t / n * 100, 0)})

    # ---- 9 月兩階段
    def phase(a, b, kw_b):
        out = {c: r(chg_bp(c, a, b)) for c in TENORS + ["TIPS10Y", "BEI10Y"]}
        out["2s10s"] = r(((lvl("UST10Y", b) - lvl("UST2Y", b)) - (lvl("UST10Y", a) - lvl("UST2Y", a))) * 100)
        out["5s30s"] = r(((lvl("UST30Y", b) - lvl("UST5Y", b)) - (lvl("UST30Y", a) - lvl("UST5Y", a))) * 100)
        out["MOVE"] = r(chg("MOVE", a, b))
        out["KW_TP"] = r(chg("KW_TP10_bp", a, kw_b))
        for c in CREDIT:
            out[c] = r(chg(c, a, b))
        return out

    phases = {"phase1": {"label": "9/1–9/22", **phase("2026-08-31", "2026-09-22", "2026-09-22")},
              "phase2": {"label": "9/23–10/1", **phase("2026-09-22", "2026-10-01", "2026-09-25")}}

    # ---- 曲線與信用水準
    curve = {}
    for day in ["2025-12-31", "2026-02-27", "2026-06-30", "2026-08-31", "2026-09-22", "2026-10-01"]:
        curve[day] = {"2s10s": r((lvl("UST10Y", day) - lvl("UST2Y", day)) * 100),
                      "5s30s": r((lvl("UST30Y", day) - lvl("UST5Y", day)) * 100),
                      "3m10y": r((lvl("UST10Y", day) - lvl("UST3M", day)) * 100)}
    credit = {}
    for c in CREDIT:
        s = df[c].dropna()
        credit[c] = {"2025-12-31": r(lvl(c, "2025-12-31")), "2026-09-22": r(lvl(c, "2026-09-22")),
                     "last": r(s.iloc[-1]), "last_day": str(s.index[-1].date()),
                     "2026_max": r(s["2026"].max()), "2026_max_day": str(s["2026"].idxmax().date()),
                     "apr2025_max": r(s["2025-04"].max()),
                     "last_pctile_2017_2025": r((s[HIST[0]:HIST[1]] < s.iloc[-1]).mean() * 100, 0)}

    summary = {"asof": str(asof.date()), "vol_table": vol_table, "ivrv_points": ivrv_points,
               "rv10_since_0923": r(rv_since_0923), "may_aug_ivrv": may_aug, "move_jump": move_jump,
               "verify": verify, "decomp": decomp,
               "phases": phases, "curve": curve, "credit": credit,
               "hist_ivrv": {"mean": r(hist_ivrv.mean()), "median": r(hist_ivrv.median()),
                             "p90": r(hist_ivrv.quantile(0.9))}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))

    wk = pd.DataFrame({"MOVE": move, "RV10_21d": rv10, "UST10Y": df["UST10Y"], "HY_OAS_bp": df["HY_OAS_bp"]})
    wk = wk["2026-01-01":].ffill().resample("W-FRI").last()
    wk.round(2).to_csv(OUT / "weekly_2026.csv")

    print(json.dumps(summary, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
