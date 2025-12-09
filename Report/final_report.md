# Income and Liquor Spending Behavior Across Iowa Counties  
## A Data-Driven Policy Analysis  
**ADEC 7900 – Course Project Final Report**

**Prepared by:**  
Shreyansh Budhia  
William Brewster  
Ramzi Nia  

---

## 1. Introduction

Our analysis was conducted for the Executive Director of the Iowa Department of Public Health, namely Mr. Larry Johnson. His organization operates in a decision environment that balances economic revenue generation, public health concerns, and community well-being. Liquor sales represent a major source of state revenue, but alcohol consumption is also associated with long-term public health and social costs.
The broader decision climate is influenced by:

•	Rising healthcare expenditures,
•	Public concerns over substance abuse,
•	And debates over how alcohol access and taxation should be structured across income groups and geographic regions.

### Research Question
**Is there a meaningful relationship between median household income and liquor spending per capita across Iowa counties?**

### Policy Relevance
Understanding whether higher-income counties consume more alcohol on a per-person basis helps decision makers:
- Evaluate the equity of alcohol taxation policies  
- Identify whether alcohol consumption burdens fall disproportionately on certain income groups  
- Determine where education, prevention, or regulatory resources should be targeted  

Policy decisions based on this analysis affect:
- State revenue collection  
- Public health planning  
- Long-term community outcomes related to alcohol misuse  

---

## 2. Data Summary

This study integrates two primary datasets covering all **99 Iowa counties**.  
- The **liquor sales dataset (2020)** reports total sales revenue, product category, and sales volume at the county level.  
- The **American Community Survey dataset (2019)** provides median household income and population by county.  

Each observation represents aggregated sales for a specific product category within a county. Because counties vary widely in population size, direct comparison of total sales alone would introduce population bias.

### Liquor Sales Dataset (2020)
- 990 transaction-level observations  
- Key fields:
  - County  
  - `sale.dollars`  
  - `sale.volume`  
  - `category`  

### American Community Survey Dataset (2019)
- 99 Iowa counties  
- Key fields:
  - `income` (median household income)  
  - `population`  
  - Education, unemployment, and demographic population shares  

---

### Table 1. Core Descriptive Statistics

| Variable | Mean | Median | Minimum | Maximum |
|---------|------|--------|----------|----------|
| Median Household Income ($) | 29,981.98 | 30,253.50 | 18,959 | 43,120 |
| Population | 31,556.47 | 15,606.50 | 3,822 | 459,159 |
| Total Liquor Sales ($) | 2,680,881.68 | 782,309.50 | 25,053 | 61,059,636 |
| Liquor Dollars Per Capita ($) | 58.50 | 55.61 | 3.57 | 220.83 |

---

### Table 2. Distribution Detail (Percentiles)

| Variable | 10% | 25% | Median | 75% | 90% |
|----------|-----|------|--------|------|------|
| Income ($) | 26,692 | 27,907.75 | 30,253.50 | 31,374 | 33,219 |
| Population | 7,365 | 10,084 | 15,606.50 | 24,894.75 | 57,141.20 |
| Sales ($) | 207,934.70 | 443,400.25 | 782,309.50 | 1,651,912 | 4,279,618.80 |
| Per Capita ($) | 25.22 | 36.62 | 55.61 | 71.08 | 95.36 |

---

### Methodological Implications
- We assume short-term income stability between 2019 and 2020  
- We transformed total liquor sales into **per-capita values**  
- An inner join by county ensured consistent geographic alignment  

---

## 3. Data Analytics

### SQL Aggregation & Validation
SQL was used to:
- Aggregate transaction-level sales into county-level totals  
- Join sales with county income and population  
- Validate completeness and remove inconsistent county labels  

**Core SQL logic:**  
SUM(sale_dollars) GROUP BY county
INNER JOIN with ACS data


---

### Feature Engineering

We first aggregated liquor sales at the county level:

**Total County Liquor Sales** = Σ `sale.dollars`  

We then constructed a per-capita spending variable:

**Liquor Dollars Per Capita** = `Total County Liquor Sales / Population`  

This transformation was essential to remove population-driven distortion.

---

### Merging Process

The sales and ACS datasets were merged by county using:
- SQL for initial validation  
- R for data cleaning and aggregation  
- Python for final analysis, correlation testing, and visualization  

All three tools produced consistent numerical results, confirming the reliability of the workflow.

---

### Correlation Analysis

We computed the Pearson correlation coefficient between:
- Median household income  
- Liquor dollars per capita  

The Pearson correlation between median household income and liquor spending per capita is:

> **r ≈ -0.106**

This indicates an extremely weak and slightly negative relationship. With **n = 99 counties**, the magnitude of the relationship is statistically and economically negligible.

Per-capita liquor spending ranges from **$3.57** at the lower end of the distribution to **$220.83** in the highest-spending counties. Total county-level liquor sales vary from approximately **$25,053** to more than **$61,059,636** annually, demonstrating that market size dominates total revenue patterns.

---

## Visualization Insights

### Figure 1. Median Household Income vs Liquor Spending Per Capita  
[Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/Tableau/income_vs_liquor_scatter.png)

- Points appear near-randomly dispersed  
- Regression line slopes slightly downward  
- Confirms weak negative relationship (r ≈ –0.106)  

This figure visualizes the relationship between county-level median household income and per-capita liquor spending. Each point represents a county, with values normalized by population to reflect individual-level consumption rather than total revenue.

---

### Figure 2. Income vs Total Liquor Sales  
[Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/sql/Income_vs_Total_Liquor_Sales_SQL.png)

A strong upward slope appears here, but this is:
- Entirely driven by population size  
- Not by individual consumption behavior  

Once sales are normalized per capita, this relationship disappears.

---

### Figure 3. Distribution of Liquor Spending Per Capita  
- Histogram: [Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/Tableau/Histogram%20-%20Per%20Capita%20Spending.png)  
- Boxplot: [Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/Tableau/Boxplot%20-%20Per%20Capita%20Spending.png)  

The distribution is right-skewed, with most counties clustered between **$30 and $80** per resident and a small number of extreme outliers exceeding **$150 per capita**.

---

### Figure 4. Correlation Matrix  
[Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/python/correlation_matrix.png)

- Income vs Per Capita: r ≈ –0.11  
- Population vs Total Sales: r ≈ 0.99  
- Population vs Per Capita: r ≈ 0.47  

This confirms that total sales are population-driven, not income-driven.

---

### Figure 5. Total Liquor Sales by County  
[Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/Tableau/Liquor%20Dollars%20Per%20Capita%20by%20County.png)

Liquor revenue is highly concentrated in Polk, Linn, Johnson, and Scott counties.

---

### Figure 6. Liquor Dollars Per Capita (Top 10)  
[Open](https://github.com/niara-crypto/Course-Project-Iowa-liquor-income-analysis-FV/blob/186611dacd2919a1c3354292c2d5cdbe4bcadd72/Tableau/Liquor%20Dollars%20Per%20Capita%20by%20County%20(Top%2010).png)

These counties represent the highest alcohol-related behavioral risk zones in the state.

---

All figures are reproduced in **Appendix A**.

---

## 4. Conclusion

This project applied a full analytical pipeline:
- Data ingestion and aggregation  
- Normalization through per-capita transformation  
- Correlation testing  
- Visualization and interpretation  
- Cross-platform validation  

### Final Answer to the Research Question

**Median household income is not a meaningful predictor of liquor spending per capita across Iowa counties.**

---

### Limitations
- Single-year analysis  
- No behavioral controls (age, tourism, density)  
- No causal inference  
- County-level averages mask within-county inequality  

---

## 5. Policy Recommendation

### Policy Decision Facing the State

The Office of the Executive Director must decide:
- Whether alcohol taxation should be income-adjusted  
- Whether public health interventions should be geographically targeted  

---

### Data-Driven Recommendation

Because income is not strongly linked to liquor consumption per capita, we recommend:

> **Targeting alcohol policy interventions based on consumption intensity and public health risk rather than income levels alone.**

---

### 1. Maintain a Uniform Statewide Alcohol Tax Structure

- Per-capita consumption is statistically independent of income  
- There is no spatial clustering of high consumption in high-income counties  

---

### 2. Target Prevention Based on Per-Capita Consumption

High-risk counties should receive:
- Alcohol education  
- Addiction treatment  
- Community-based intervention  
- Youth substance-abuse prevention  

---

### 3. Use High-Revenue Counties for Enforcement Only

Polk, Linn, Johnson, and Scott counties should be prioritized for:
- Retail compliance  
- Distributor auditing  
- Supply chain enforcement  
- Revenue forecasting
  

---

### First-Order Policy Effects

- More efficient allocation of prevention funding  
- Elimination of income-based misclassification of high-risk counties  
- Improved targeting accuracy for addiction services  
- Stronger alignment between policy tools and behavioral data  

---

### Second-Order Policy Effects

- Reduction in long-term alcohol-related healthcare costs  
- Lower incidence of alcohol-related crime and injury  
- Improved labor productivity and workforce stability  
- Stabilization of state liquor revenue without inequitable taxation  

---

### Benefits

- Evidence-based targeting  
- Reduced waste in prevention spending  
- Higher return on public health investment  
- Policy fairness across income groups  
- Improved community health outcomes  

---

### Risks

- Public resistance if high-consumption counties feel singled out  
- Short-term revenue volatility in affected counties  
- Community stigma  

---

### Risk Mitigation Strategies

These risks can be mitigated through:

- Transparent data communication  
- Gradual implementation  
- Community-based education programs  

---

### Final Executive Policy Conclusion

Income is not a meaningful driver of liquor consumption behavior in Iowa.

Alcohol policy should therefore be structured around observed **per-capita consumption intensity**—not income, and not total revenue.

Uniform taxation combined with geographically targeted public health intervention in high-consumption counties represents the most efficient, equitable, and economically sound alcohol policy strategy for the State of Iowa.


---

## Appendix A – Figures

1. Income vs Per-Capita Spending  
2. Income vs Total Sales  
3. Histogram & Boxplot  
4. Correlation Matrix  
5. Total Sales by County  
6. Top 10 Per-Capita Counties
