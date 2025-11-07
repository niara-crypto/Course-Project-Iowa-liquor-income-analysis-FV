library(tidyverse)

# Load
sales <- read_csv("project.sales.counties.csv")
acs   <- read_csv("project.acs.counties.csv")

# Aggregate sales to county
sales_county <- sales %>%
  group_by(county) %>%
  summarise(total_sales_dollars = sum(sale.dollars, na.rm = TRUE),
    .groups = "drop")

# Prep ACS (rename income for clarity)
acs_county <- acs %>%
  select(county, income, population) %>%
  rename(median_household_income = income)

# Merge + dollars per capita
merged <- sales_county %>%
  inner_join(acs_county, by = "county") %>%
  mutate(dollars_per_capita = total_sales_dollars / population)

# Quick KPI: correlation
cor(merged$median_household_income, merged$dollars_per_capita, use = "complete.obs")

# Save for Tableau
write_csv(merged, "merged_county_data_for_tableau.csv")
