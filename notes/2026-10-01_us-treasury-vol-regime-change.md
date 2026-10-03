# 美債 Vol 的定價轉變 — 內容整理

> - 原文：【市況觀察 — 美債 Vol 的定價轉變】（資料時點：2026/10/1）
> - 整理日期：2026/10/3
> - 第 0～10 節依原文順序整理；第 11～12 節為整理者補充（名詞速查、閱讀筆記），非原文觀點

---

## 0. 一段話看懂全文

本輪美債拋售主要由**實質利率**推動（政策利率預期上修 ＋ AI 投資競逐長期資本），而非通膨預期脫錨或財政溢價上升。在這種「**預期主導**」的行情裡，選擇權買方不願多付保險費，Swaption Implied Vol 反而被壓在低檔（VRP 萎縮）。近期短率轉為震盪、**TP 反彈**、MOVE 同步勁揚至 110，作者認為美債（尤其 Vol）的定價可能正從「預期主導」轉向「**TP 主導**」，也就是 **Regime Change**。MOVE 上升主要反映長端 Buy Side 的避險與停損，短期內不必然觸發去槓桿與跨市場 Risk-Off，但會加速削減信用市場的 Buffer。

---

## 1. 市況背景

### 1.1 關鍵數據

| 項目 | 數據 / 描述 |
|---|---|
| 10Y 美債殖利率 | 10/1 一度觸及 **5.34%**，創 2002 年以來新高 |
| 美伊開戰以來累計 | 上漲**超過 130 bp** |
| 9 月單月 | 上行約 **60 bp** |
| 上行來源拆解 | 實質利率貢獻約 **120 bp**；其餘（推算約 10 餘 bp）來自 BEI 與 TP |
| 2026/5–9 | 10Y 自 **4.3%** 一路升至接近 **5.3%** |
| 同期 3m10y Swaption IV | 停滯在 **70–80 bp/y** 的歷史低檔區間 |
| MOVE | 10/1 升至 **110**，接近 2026/3 月底的高點 |
| 對照：2025/4 關稅戰 | MOVE 飆到 **140** |

### 1.2 時間軸

| 時間 | 事件 |
|---|---|
| 2025/4 | 關稅戰觸發股市 Sell-Off → 追繳保證金踩踏、Basis Trade 大量 Unwind → MOVE 飆到 140 |
| 2026/3 月底 | MOVE 前波高點 |
| 2026/5–9 | 10Y 4.3% → 接近 5.3%，但 3m10y Swaption IV 停在 70–80 bp/y |
| 2026/9 | Warsh 升息，之後通膨預期下降；10Y 單月上行約 60 bp |
| 近期（至 10/1） | 升息預期不再往右尾定價、短率轉震盪；但 TP 反彈、長率續升；MOVE 幾乎同時勁揚 |
| 2026/10/1 | 10Y 一度觸及 5.34%；MOVE 升至 110 |

文中未註明日期的事件：美伊開戰（至今 10Y 累計上漲超過 130 bp）、Warsh 上任 Fed 主席後大幅削減 Forward Guidance、Bessent 擴大公債回購（之後 TP 回落）。

> 「TP 在回購後回落」與「近期 TP 反彈」指的是不同時段（先降後升），兩者並不矛盾。

---

## 2. 本輪拋售的驅動：「不是什麼」vs.「是什麼」

### 2.1 不是：與市場熱烈討論的方向不同

| 市場流行的說法 | 作者的反駁依據 |
|---|---|
| 能源衝擊使通膨預期脫錨（BEI ↑） | 通膨預期在 **Warsh 9 月升息後下降** |
| 政府大量發債使 Fiscal Premium 上升（TP ↑） | TP 在 **Bessent 擴大回購後回落** |

作者評價：兩位都做到「當前能力範圍內最正確的決定」，而且也都有效果。

### 2.2 是：實質利率急遽上升，主因兩點

1. **未來政策利率預期提升**
2. **AI 投資對長期資本的競逐**

而且第 2 點又會進一步推升第 1 點。

---

## 3. 近期變化 → 兩個核心問題 → Regime Change 預告

### 3.1 近期變化

- 升息預期不再往右尾定價 → **短率轉為震盪**
- 但 **TP 反彈** → 長率延續上行
- **MOVE 幾乎同時勁揚**，10/1 升至 110，接近 2026/3 月底的高點

### 3.2 作者提出的兩個問題

- **Q1**：債市已經被激進做空一個多月，為何 MOVE 此時才上升？
- **Q2**：這是否代表對股市的壓力及去槓桿即將到來？

### 3.3 預告

若短期內**戰事與基本面的路徑沒有太大變化**，接下來美債（尤其 Vol）的定價或將迎來 **Regime Change**。

Q1 由第 4～7 節的框架回答，Q2 由第 8 節回答，兩題的答案彙整在第 9 節。

---

## 4. 異常現象：殖利率噴出，IV 卻停在低檔

| | 內容 |
|---|---|
| 傳統市場邏輯 | 利率越高 → 終端政策利率與財政可持續性的不確定性越大 → 波動度理應同步擴張 |
| 實際觀察（2026/5–9） | 10Y 自 4.3% 噴出至接近 5.3%，但基準 3m10y Swaption IV 停滯在 70–80 bp/y 歷史低檔 |
| 解謎關鍵 | 剖析 Yield Variance 的「底層驅動因素」 |

---

## 5. 分析框架

### 5.1 殖利率拆解

- 美債殖利率 = 實質利率（TIPS）＋ 通膨預期（BEI）＋ Term Premium（TP）
- 因此 Nominal Yield − TIPS = BEI ＋ TP

### 5.2 變異數拆解

依 Philadelphia Fed 的專業預測者調查（**SPF**）與 **Kim-Wright Term Structure Model**，10Y 美債的變異數可拆為：

```
Yield Variance = Var(Expectation Shocks)
               + Var(Term Premium Shocks)
               + 2 × Cov(Expectations, Term Premium)
```

### 5.3 核心命題

- 選擇權買方主要願意為 **Term Premium Shocks** 支付額外的風險補償
- 當利率變動主要由央行政策路徑的 **Expectation Shocks** 驅動時，**VRP 反而萎縮**

### 5.4 VRP 的定義

- VRP = 隱含波動度 − 未來實現波動度（**IV − RV**）
- 本質是選擇權買方向賣方支付的「保險費」
- 當利率變化的主導力量在 TP 與政策預期之間切換時，買方的支付意願與定價機制會顯著分化

### 5.5 造成分化的四個原因（第 6 節逐一展開）

1. 避險工具的可替代性
2. Realized 與 Implied Vol 的動態壓縮
3. 風險分佈的邊界與尾端特質存在本質差異
4. 交易者結構與市場博弈心理

---

## 6. 四大機制逐一拆解

### 6.1 機制一：避險工具的替代性 —「線性風險好對沖，非線性尾端風險難對沖」

**(A) Policy Expectation Shocks：可由低成本線性工具直接覆蓋**

- 驅動：總經數據（NFP、CPI、PCE）＋ 央行的 Reaction Function，即 Data Dependent
- 性質：方向性、具清晰宏觀邏輯、流動性高
- 可用工具：SOFR Futures、Fed Funds Futures、SOFR OIS、Fed Funds OIS、T-Bills
  - 深度佳、交易成本低，能精準 Mapping DV01
- 結果：既然能用極低成本的工具管理利率風險，就沒必要為選擇權（Non-Linear Convexity Tools）支付昂貴 Premium，還得管理複雜的 Greeks → **壓低買方對 Short Expiry Option 的額外補償意願**

**(B) Term Premium Shocks：難以用線性工具消除的結構性風險**

- TP 反映的結構性失衡：
  - 財政赤字失控
  - 國債供給消化不良
  - 流動性枯竭
  - 地緣政治動盪
  - 外國官方買家退場、國內私人機構持有增加
- 通常伴隨市場微結構的破壞：
  - Market Maker 的資產負債表受限
  - Repo Haircut 加大
  - 跨資產避險失效（如股債負相關性失靈）
- 避險者：Liability Driven 的 Pension Funds、Lifers、Sovereign Funds
- 面對的風險：未知的供給吸收障礙與失序拋售 → **無錨定上限的極端右尾風險**
- 需要的工具：非線性凸性保護（如 **Deep OTM Payer Swaptions**）
- 結果：避險需求高度 **Price-Inelastic**，願意支付遠超常態的保險費

### 6.2 機制二：RV 劇烈釋放，擠壓 IV 與 RV 的利差空間

**(A) 預期主導期：RV 大幅飆升，推高賣方 Delta Hedging 成本**

- 每次重要經濟數據公布或央行會議，利率都會出現方向明確的大幅跳空與趨勢性行情 → RV 顯著拉高
- Warsh 上任主席後大幅削減 Forward Guidance → 進一步放大每次重要數據公布的市場反應
- 對選擇權賣方（Short Gamma）：劇烈波動下進行 Dynamic Delta Hedge，產生大量「追高殺低」的 Gamma 損耗 → 侵蝕收進來的 Time Value

**(B) IV 存在宏觀錨定上限，無法等比例擴張**

- 政策利率預期不會無限發散，受中性利率（r*）、Taylor Rule 與潛在經濟增速約束 →（理論上）利率不可能無止境上升而不引發衰退
- 因此選擇權市場對政策利率的 IV 往往在合理區間內被「錨定」
- 過去一段時間，大量系統性做空波動度的 Hedge Funds 積極壓低 IV → 即便殖利率持續走揚，波動度仍維持低位
- RV 因宏觀數據衝擊而放大、IV 又受理論上限壓制 → 兩者差距萎縮 → **Sell Vol 的 VRP 縮水**
- 這是近期 **Sell Vol Flow 逐漸退場**的另一個底層原因

### 6.3 機制三：不確定性的分佈特徵 — 有邊界的常態分佈 vs. 肥尾的黑天鵝

**(A) 預期衝擊：「條件均值回歸」的相對有界分佈**

- 市場修正政策路徑，本質是在預測央行何時達到 Terminal Rate
- 升息達到一定高度 → 市場自發定價貨幣緊縮對經濟的冷卻效果 → 抑制利率 Upside
- 雙向牽制 → 機率分佈偏向均值回歸、缺乏 Fat Tails → **Tail Risk Premium 較低**

**(B) 期限溢價衝擊：「自我強化」與「非對稱肥尾」**

- 財政供給過剩與 TP 上升之間**不存在天然的經濟煞車機制**
- 殖利率飆升 → 融資抵押品追繳保證金（如 2022 年英國 LDI 危機）→ 倒逼機構進一步拋售現貨
- 惡性循環：**拋售 → 波動度上升 → VaR 上限觸發 → 進一步拋售**
- 選擇權 Market Maker 面對缺乏基本面定錨的 Tail Shock，為了防範資產負債表爆倉，會在報價中加上較高的 Risk Premium 與 Liquidity Premium → **推升 TP 主導環境下的 VRP**

### 6.4 機制四：交易者結構與市場博弈心理

**(A) 預期主導：套利資本充沛，市場理性定價**

- 主要參與者：宏觀對沖基金、相對價值（RV）基金、量化交易者
- 對利差與定價偏差高度敏感 → IV 稍有偏高，套利資本便迅速進場 Sell Vol、賺取 Time Value → **把 VRP 壓回合理水位**

**(B) TP 主導：被動避險與監管剛性需求激增**

- 情境：市場擔憂主權債信譽受損、長債發行量增加
- 買方：需要滿足資本適足率、償付能力監管標準，或匹配 Asset Liability Risk 的機構
- 動機：以資本安全與監管合規為首要考量，而非短期交易獲利 → **更願意接受較高的 VRP** → 墊高整個選擇權市場的價格

---

## 7. Swaptions 策略意涵

| 環境 | 特徵 | 對 Short Vol 的意涵 |
|---|---|---|
| **預期主導期** | 宏觀數據受高度重視，市場積極重定價央行升降息路徑 | 單純 Short Gamma 容易遭 RV 上揚侵蝕，**風報比低** |
| **TP 主導期** | 政策路徑大致清晰，市場轉向定價「消化長端公債供給與財政赤字需要多少溢價」 | IV 往往因 Hedging Panic 而 Overvalued → 對尋求短期獲利的機構 Trader，是**系統性做空並變現 VRP 的較佳窗口** |

> ⚠️ 作者提醒：當前債市的右尾風險肯定也不低，尤其 **AI Financing 也加入長端資本競逐**。

---

## 8. 總結：MOVE 上升代表什麼？會不會引發去槓桿？

### 8.1 MOVE 上升的本質

- 是 Implied Vol 被**系統性抬升**的結果
- 反映持有 Long End Duration Exposure 的大型 Buy Side 機構開始**加大避險與停損力度**

### 8.2 不代表短期內會立即大幅去槓桿、跨市場轉向 Risk-Off

- Hedge Funds 持有美債的規模雖持續增加（補上 Fed 及海外央行減持的部分）
- 但在 **eSLR 放寬後**，Basis Trade 的操作規模已逐漸移轉至 **G-SIBs**
- 這些 Primary Dealers 對價格的敏感度與調倉頻率不如 Hedge Funds → **Repo Market 的脆弱性有所改善**

### 8.3 歷史對照：2025/4 關稅戰

- 股市 Sell-Off → 追繳保證金踩踏 → Basis Trade 大量 Unwind → MOVE 飆到 140
- 現在重演的可能性小了許多

### 8.4 仍值得注意

- MOVE 出現 **High Level Clustering** 時，仍很難不引起 Rates Trader、Bond Trader 及 Credit Trader 的注意
- MOVE 長時間維持高位（Outright Yields 持續上行）不一定馬上使股市估值修正，因為 AI Narratives 仍是能硬扛高殖利率的 Solid Story
- 但這**無疑正在加速削減信用市場的 Buffer 與風險承受力**

---

## 9. 回到開頭的兩個問題

**Q1：債市已被激進做空一個多月，為何 MOVE 現在才上升？**

依作者的框架，可以串成三步：

1. 5–9 月的上行以「預期主導」為主 → 線性工具即可避險、IV 被 r* / Taylor Rule 錨定、分佈有界、套利資本積極 Sell Vol → VRP 萎縮，IV 停在 70–80 bp/y
2. 同時 RV 放大、IV 被壓 → Short Vol 的獲利空間（VRP）縮水 → Sell Vol Flow 逐漸退場，壓低 IV 的力量變弱
3. 近期短率轉為震盪、TP 反彈 → 驅動力轉向 TP → 長端 Buy Side 加大避險與停損（Price-Inelastic 的凸性需求）→ IV 被系統性抬升 → MOVE 升至 110

**Q2：是否代表股市壓力與去槓桿即將到來？**

作者認為短期內不會立即觸發大幅去槓桿與跨市場 Risk-Off：

- eSLR 放寬後 Basis Trade 部位逐漸移往 G-SIBs，Repo 市場脆弱性改善
- 與 2025/4（MOVE 140、Basis Trade 踩踏）相比，重演的可能性小很多
- 股市有 AI Narrative 撐著，壓力會先體現在**信用市場 Buffer 的削減**；MOVE 高位群聚仍值得 Rates / Bond / Credit Trader 警惕

---

## 10. 一頁總覽

### 10.1 對照總表：預期主導 vs. TP 主導

| 面向 | 預期主導（Expectation Shocks） | TP 主導（Term Premium Shocks） |
|---|---|---|
| 驅動因素 | 總經數據 ＋ 央行 Reaction Function（Data Dependent） | 財政赤字、國債供給、流動性、地緣政治、持有者結構 |
| 避險工具 | 線性工具：SOFR / FF Futures、OIS、T-Bills | 非線性凸性：Deep OTM Payer Swaptions |
| 買方價格彈性 | 高（有便宜的替代品） | 極低（Price-Inelastic） |
| RV vs. IV | RV 飆升、IV 被錨定 → IV − RV 被壓縮 | IV 因 Hedging Panic 被抬升，容易 Overvalued |
| 分佈特徵 | 條件均值回歸、相對有界、缺乏肥尾 | 自我強化、非對稱肥尾、無天然煞車 |
| 主要參與者 | 宏觀 HF、RV 基金、量化交易者 | Pension Funds、Lifers、Sovereign Funds |
| VRP 的定價力量 | 套利資本 Sell Vol，把 VRP 壓回合理水位 | 做市商加上 Risk / Liquidity Premium，剛性買盤接受高 VRP |
| VRP | 萎縮 | 擴張 |
| Short Vol 策略 | 風報比低 | 較佳窗口（但須留意右尾） |
| 本文對應 | 2026/5–9：10Y 4.3% → 接近 5.3%，IV 停在 70–80 bp/y | 近期跡象：短率震盪、TP 反彈、MOVE 升至 110（作者認為接下來可能轉入此 Regime） |

### 10.2 整體邏輯鏈

```
美伊開戰
  └─ 實質利率急升（130+ bp 中約 120 bp）
       ├─ 政策利率預期上修
       └─ AI 投資競逐長期資本（並回頭推升政策利率預期）
                    ↓
2026/5–9「預期主導」：10Y 4.3% → 接近 5.3%
  ├─ 線性工具即可避險 → 不需付高 Premium 買選擇權
  ├─ RV ↑、IV 被 r* / Taylor Rule 錨定 → IV − RV 被壓縮
  ├─ 分佈均值回歸、缺乏肥尾 → Tail Risk Premium 低
  └─ 套利資本積極 Sell Vol
                    ↓
VRP 萎縮、IV 停在 70–80 bp/y；Short Vol 獲利空間縮水 → Sell Vol Flow 逐漸退場
                    ↓
近期：升息預期不再往右尾定價、短率震盪；但 TP 反彈、長率續升
                    ↓
長端 Buy Side 加大避險與停損 → IV 被系統性抬升 → MOVE 升至 110（10/1）
                    ↓
可能的 Regime Change：預期主導 → TP 主導（前提：戰事與基本面路徑沒有大變化）
  ├─ 策略：TP 主導下 IV 易 Overvalued → Short Vol 的較佳窗口
  │         （但右尾風險不低：AI Financing 也在競逐長端資本）
  └─ 風險：去槓桿機率低於 2025/4（eSLR 放寬、Basis Trade 移往 G-SIBs）
            但信用市場的 Buffer 與風險承受力正被削減
```

---

## 11. 名詞速查（整理者補充）

### 波動度與選擇權

| 名詞 | 說明 |
|---|---|
| MOVE Index | ICE BofA 編製的美債選擇權隱含波動度指數（1 個月期，2Y/5Y/10Y/30Y 加權），以 bp 表示，常被稱為「債市 VIX」 |
| 3m10y Swaption | 3 個月後到期、標的為 10 年期利率交換（IRS）的選擇權；Vol 以 Normal Vol（bp/y）報價 |
| bp/y 換算 | 年化 Normal Vol ÷ √252 ≈ 每日 1 個標準差的波動：70–80 bp/y ≈ 每日 4.4–5.0 bp；MOVE 110 ≈ 6.9 bp；MOVE 140 ≈ 8.8 bp |
| IV / RV | Implied Vol（選擇權價格隱含的預期波動）／ Realized Vol（實際發生的波動） |
| VRP | Volatility Risk Premium ＝ IV − 未來 RV，選擇權買方付給賣方的「保險費」 |
| Payer Swaption | 有權「支付固定、收取浮動」的利率交換選擇權，利率上升時獲利；Deep OTM Payer 用來保護利率右尾 |
| Short Gamma / Delta Hedging | 賣出選擇權者為維持 Delta 中性需動態避險，波動劇烈時被迫追高殺低，產生 Gamma 損耗 |
| Time Value | 權利金中的時間價值，是選擇權賣方的主要收益來源 |
| Greeks | 選擇權風險參數（Delta、Gamma、Vega、Theta 等） |

### 殖利率拆解

| 名詞 | 說明 |
|---|---|
| TIPS | 抗通膨公債，其殖利率視為實質利率 |
| BEI | Breakeven Inflation ＝ 名目殖利率 − TIPS 殖利率，市場隱含的通膨預期 |
| TP（Term Premium） | 持有長債（相對於滾動持有短債）所要求的額外補償 |
| SPF | Philadelphia Fed 每季發布的專業預測者調查（Survey of Professional Forecasters） |
| Kim-Wright Model | Fed 研究員 Don Kim 與 Jonathan Wright 提出的三因子無套利期限結構模型，用來拆解「利率預期」與「TP」，Fed 官網定期更新估計值 |

### 政策利率與工具

| 名詞 | 說明 |
|---|---|
| r* | 中性利率：既不刺激也不緊縮經濟的實質政策利率 |
| Terminal Rate | 本輪升息循環預期的最高點 |
| Taylor Rule | 依通膨缺口與產出缺口推算政策利率的經驗法則 |
| Forward Guidance | 央行對未來政策路徑的前瞻指引 |
| SOFR / OIS | 擔保隔夜融資利率／隔夜指數交換，市場用來交易政策利率路徑 |
| DV01 | 殖利率變動 1 bp 對應的價值變化，用來計算對沖比例 |

### 市場結構與機構

| 名詞 | 說明 |
|---|---|
| Basis Trade | 買進現貨美債、放空公債期貨，以 Repo 融資賺取兩者基差的高槓桿交易 |
| Repo Haircut | 以債券做 Repo 融資時抵押品的折價比率；加大代表融資條件收緊、槓桿空間縮小 |
| eSLR | enhanced Supplementary Leverage Ratio，美國 G-SIBs 的補充槓桿率要求；放寬後銀行資產負債表較能承接美債部位與 Repo 中介 |
| G-SIBs | 全球系統性重要銀行 |
| Primary Dealers | 紐約 Fed 指定的公債一級交易商（多隸屬大型銀行） |
| LDI | Liability-Driven Investment（負債驅動投資）；2022 年英國 LDI 危機：英債殖利率飆升 → 退休金 LDI 部位被追繳保證金 → 被迫拋售英債 → 殖利率再飆，最後由英格蘭銀行進場干預 |
| Lifers | 壽險公司 |
| VaR | Value at Risk（風險值）；機構多設有 VaR 上限，波動上升推高 VaR 時被迫減碼 |
| High Level Clustering | 波動度在高檔持續聚集（Volatility Clustering） |
| Hedging Panic | 恐慌性避險買盤 |

---

## 12. 閱讀筆記（整理者補充，非原文觀點）

1. **拆解口徑**：文中「Nominal − TIPS = BEI ＋ TP」是簡化寫法。市場口徑下 Nominal − TIPS 就是 BEI，而 BEI 除了通膨預期，也含通膨風險溢酬並受 TIPS 流動性影響；同時 TIPS 實質殖利率本身也含有實質期限溢酬（Real TP），Kim-Wright 估的則是名目 TP。因此「實質利率貢獻約 120 bp」不必然代表 TP 的貢獻很小，部分實質殖利率上行可能落在 Real TP（作者則將其歸因於政策路徑與 AI 資本競逐）。把「市場口徑：Nominal = Real ＋ BEI」與「模型口徑：Yield = 利率預期 ＋ TP」分開看，比較容易理解「實質利率主導」與「TP 反彈」為何能同時成立。

2. **AI 的雙重角色**：AI 在文中出現兩次：（a）AI 投資競逐長期資本並推升政策利率預期（可理解為 r* 或成長預期上移，偏「預期成分」）；（b）AI Financing 加入長端資本競逐（長端供給壓力，偏「TP 成分」）。若（b）加速（例如長天期公司債大量發行），會強化 TP 主導與右尾風險，這正是作者對 Short Vol 策略的主要提醒。

3. **判斷的前提**：Regime Change 的判斷建立在「短期內戰事與基本面路徑沒有太大變化」。若戰事升級帶來能源衝擊（BEI 重新上行），或數據大幅意外使市場再度重定價政策路徑（回到預期主導），結論就需要調整。

4. **可追蹤的驗證指標**：
   - TP：Kim-Wright（Fed）、ACM（NY Fed）的 10Y Term Premium
   - 政策路徑：SOFR Futures / OIS 隱含的利率路徑是否維持震盪
   - 實質利率與通膨預期：10Y TIPS 殖利率、10Y BEI
   - Vol 與 VRP：MOVE、3m10y Swaption Normal Vol，以及 IV 與 RV 的差距
   - 右尾避險需求：Payer Swaption Skew（OTM Payer 相對 ATM 的 Vol 溢價）
   - 融資與去槓桿壓力：SOFR 與 IORB 利差、Swap Spread、Treasury Futures Basis
   - 信用市場 Buffer：IG / HY Credit Spread
