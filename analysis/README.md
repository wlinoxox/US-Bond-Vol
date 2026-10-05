# 資料統整與分析

Bloomberg 資料受授權限制，而這個 repo 是公開的，所以原始資料與統整後的資料都放在 `data/private/`（已列入 `.gitignore`），只有程式碼和分析結論會推上 repo。

## 流程

1. 把 Bloomberg 匯出的兩份 Excel 放進 `data/private/raw/`：
   - `bbg_template.xlsx`：MoveRates 範本（MOVE、HY / IG OAS、CDX IG / HY、3M / 2Y / 5Y / 10Y / 30Y 殖利率，2016/10 起），每個 ticker 一組「日期／數值」，已貼成值
   - `us_bond_vol_rv_iv_refreshed.xlsx`：`excel/us_bond_vol_rv_iv.xlsx` 在 Bloomberg 重新整理後存檔的版本（10Y、SOFR swap、TIPS、BEI、MOVE，2024 起）
2. `python analysis/consolidate.py`：統整成 `data/private/market_daily.csv` 與 `market_daily.xlsx`（附欄位說明），再併入 Kim-Wright 與 DKW。
3. `python analysis/analyze.py`：輸出 `data/private/analysis/summary.json`（筆記與簡報的數字來源）與 `weekly_2026.csv`（簡報圖表用）。

## 統整時處理的問題

| 問題 | 處理方式 |
|---|---|
| 舊版 Excel 範本的 MOVE BDH 回傳每個日曆日（含週末）且隱藏日期，依列對齊會和其他欄位錯位 | 依「起始日起算的日曆日」重建日期，與 `bbg_template` 附日期的 MOVE 比對，688 個重疊日完全一致後才採用。新版範本已改成每組 BDH 輸出自己的日期、依日期比對 |
| `bbg_template` 最後一天是盤中快照（10/2 的 10Y 快照 5.2495%，收盤 5.2706%） | 捨棄快照日；10Y 與 MOVE 的 10/2 收盤由較晚抓取的 Excel 補上 |
| 重新整理日（10/5）的數值是亞洲盤中價或沿用前值 | 截止日取 MOVE 最後一次更新的日期（10/2） |
| `Fill=P` 讓假日的數值沿用前一天 | 計算 RV 時，變動恰為 0 的日子不計入 |
| HY / IG OAS 在範本中以 % 呈現 | 乘以 100 換成 bp |

## 指標定義

- **RV**：最近 21 個每日變動（bp）的樣本標準差 × √252，至少 18 筆有效資料
- **IV − RV**：MOVE − 10Y 21 日 RV（MOVE 是 1 個月期選擇權）
- **事後 VRP**：當日 MOVE − 之後 21 個交易日實際發生的 10Y RV
- **百分位**：相對 2017–2025 年的分布
