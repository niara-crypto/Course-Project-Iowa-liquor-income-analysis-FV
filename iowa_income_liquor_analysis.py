# iowa_income_liquor_analysis.py
"""
Checkpoint 2 - Iowa Liquor Sales vs Income (County level)


Outputs created in the *IowaCheckpoint2_Python* folder:
    - merged_county_data_for_python.csv
    - income_vs_liquor_scatter.png
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------
# PATHS
# ------------------------------------------------------------------

# Folder where THIS script lives: .../IowaCheckpoint2_Python/Scripts
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root: .../IowaCheckpoint2_Python
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Data folder: .../IowaCheckpoint2_Python/Data
DATA_DIR = os.path.join(PROJECT_DIR, "Data")

SALES_FILE = "project.sales.counties.csv"
ACS_FILE   = "project.acs.counties.csv"

sales_path = os.path.join(DATA_DIR, SALES_FILE)
acs_path   = os.path.join(DATA_DIR, ACS_FILE)

print("Using data files:")
print("  Sales:", sales_path)
print("  ACS  :", acs_path)

# ------------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------------

sales = pd.read_csv(sales_path)
acs   = pd.read_csv(acs_path)

print("\nColumns in sales file:")
print(list(sales.columns))

print("\nColumns in ACS file:")
print(list(acs.columns))

# ------------------------------------------------------------------
# COLUMN NAME SETTINGS (already customized to your files)
# ------------------------------------------------------------------

SALES_COUNTY_COL   = "county"
SALES_DOLLARS_COL  = "sale.dollars"

ACS_COUNTY_COL     = "county"
ACS_INCOME_COL     = "income"
ACS_POP_COL        = "population"

# ------------------------------------------------------------------
# AGGREGATE SALES TO COUNTY LEVEL
# (If project.sales.counties.csv is already county-level totals, this
# groupby will just keep it the same. It’s safe either way.)
# ------------------------------------------------------------------

sales_county = (
    sales
    .groupby(SALES_COUNTY_COL, as_index=False)[SALES_DOLLARS_COL]
    .sum()
    .rename(columns={SALES_DOLLARS_COL: "total_sales_dollars"})
)

print("\nSales aggregated to county level (first 5 rows):")
print(sales_county.head())

# ------------------------------------------------------------------
# SELECT NEEDED ACS COLUMNS
# ------------------------------------------------------------------

acs_subset = acs[[ACS_COUNTY_COL, ACS_INCOME_COL, ACS_POP_COL]].copy()
acs_subset = acs_subset.rename(columns={
    ACS_COUNTY_COL: "county",
    ACS_INCOME_COL: "income",
    ACS_POP_COL: "population"
})

print("\nACS subset (first 5 rows):")
print(acs_subset.head())

# ------------------------------------------------------------------
# MERGE SALES + ACS ON COUNTY
# ------------------------------------------------------------------

merged = pd.merge(
    sales_county,
    acs_subset,
    on="county",
    how="inner"
)

print("\nMerged data (first 5 rows):")
print(merged.head())

# ------------------------------------------------------------------
# COMPUTE DOLLARS PER CAPITA
# ------------------------------------------------------------------

merged["dollars_per_capita"] = merged["total_sales_dollars"] / merged["population"]

# ------------------------------------------------------------------
# CORRELATION
# ------------------------------------------------------------------

corr = merged["dollars_per_capita"].corr(merged["income"])
print("\nCorrelation between income and liquor dollars per capita:", corr)

# ------------------------------------------------------------------
# SAVE MERGED DATA
# ------------------------------------------------------------------

out_csv = os.path.join(PROJECT_DIR, "merged_county_data_for_python.csv")
merged.to_csv(out_csv, index=False)
print("Merged dataset saved to:", out_csv)

# ------------------------------------------------------------------
# SCATTER PLOT + REGRESSION LINE
# ------------------------------------------------------------------

x = merged["income"]
y = merged["dollars_per_capita"]

# Fit simple linear regression y = m x + b
m, b = np.polyfit(x, y, 1)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.7, label="Counties")
plt.plot(x, m * x + b, linewidth=2, label="Best-fit line")

plt.xlabel("Median household income (ACS, counties)")
plt.ylabel("Liquor dollars per capita (2012–2016)")
plt.title("Income vs Liquor Spending per Capita (Iowa counties)")
plt.legend()
plt.tight_layout()

plot_path = os.path.join(PROJECT_DIR, "income_vs_liquor_scatter.png")
plt.savefig(plot_path, dpi=300)

print("Scatter plot saved to:", plot_path)

print("\nInterpretation hint:")
print(f"r ≈ {corr:.3f} →")
if corr < 0:
    print("Negative correlation: higher-income counties spend slightly LESS per capita on liquor.")
elif corr > 0:
    print("Positive correlation: higher-income counties spend slightly MORE per capita on liquor.")
else:
    print("No correlation between income and liquor spending per capita.")

