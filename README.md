# US-Bond-Vol

美債波動度（US Treasury Vol）相關的市況觀察與筆記。

## 筆記

| 日期 | 主題 |
|---|---|
| 2026-10-01 | [美債 Vol 的定價轉變 — 內容整理](notes/2026-10-01_us-treasury-vol-regime-change.md) |

## 簡報

| 日期 | 檔案 |
|---|---|
| 2026-10-03 | [美債 Vol 的定價轉變：TP 已回來，Vol 才剛開始定價](slides/2026-10-03_us-treasury-vol-regime-change.pptx)（凱基範本，13 頁） |

## 工具

| 檔案 | 說明 |
|---|---|
| [excel/us_bond_vol_rv_iv.xlsx](excel/us_bond_vol_rv_iv.xlsx) | Bloomberg BDH 抓 10Y 殖利率、Swap、MOVE、Swaption IV，計算 RV、IV − RV、事後 VRP，拆解 10Y = TIPS + BEI 與 DKW 四成分，並對照 Kim-Wright TP |
| [excel/build_workbook.py](excel/build_workbook.py) | 重新產生上面的 Excel（更新 Kim-Wright 資料後執行）；`--sample` 產生模擬數據測試檔 |
| [data/THREEFYTP10.csv](data/THREEFYTP10.csv) | Kim-Wright 10Y Term Premium（FRED：THREEFYTP10，單位 %，日資料） |
| [data/DKW_updates.csv](data/DKW_updates.csv) | D'Amico-Kim-Wei 拆解（Fed staff，單位 %，每月更新）：預期實質短率、實質 TP、預期通膨、通膨風險溢酬、TIPS 流動性溢酬 |
