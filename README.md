# Income and Liquor Spending Behavior Across Iowa Counties

This repository contains the complete analytical workflow for a graduate-level data analytics project examining the relationship between **median household income** and **liquor spending per capita** across all **99 Iowa counties**. The analysis supports a **policy decision-making framework** for the Iowa Department of Public Health and state revenue officials.

---

## Research Question

**Is there a meaningful relationship between median household income and liquor spending per capita across Iowa counties?**

---

## Decision-Maker Audience

This project is designed for:
- Executive Director, Iowa Department of Public Health (Iowa), Mr. Larry Johnson 

The objective is to inform:
- Alcohol taxation strategy  
- Public health prevention targeting  
- Resource allocation efficiency  

---

## Tools & Methods

- **SQL** – Aggregation, validation, and county-level joins  
- **Python** – Correlation analysis, histograms, boxplots, and heatmaps  
- **R / R Markdown** – Data cleaning and feature engineering  
- **Tableau** – Interactive dashboards and geographic visualization  
- **Excel / CSV** – Intermediate structured outputs  

---

## Key Analytical Result

- **Pearson Correlation (Income vs Per-Capita Liquor Spending):**
  - **r ≈ −0.106**
  - Indicates an **extremely weak and statistically negligible negative relationship**
- **Interpretation:**
  - Higher-income counties **do not consume more liquor per person**
  - Total liquor revenue is driven by **population size**, not income

---

## 🗂️ Repository Structure

Checkpoint/ → Course progress checkpoints
PowerPointPresentation/ → Presentation slides used in the final recording
R/ → R scripts and R Markdown workflow
Recording/ → Final group recording (if required)
Report/ → Final written policy report (PDF)
Tableau/ → Tableau dashboards and visualization outputs
data/ → County-level datasets (CSV)
python/ → Python analysis scripts and figures
sql/ → SQL queries and outputs

.gitattributes
.gitignore
README.md


---

## How to Reproduce the Core Analysis

1. Run the R Markdown cleaning script:

R/Module8Project.Rmd

2. Use the processed dataset located in:
data/
3. Run Python correlation & visualizations from:
python/
4. Open Tableau dashboards from:
Tableau/


---

## Final Deliverables

- Final Policy Report (PDF)
- Python Correlation & Distribution Visuals
- Tableau Interactive Dashboards
- Group Presentation Slides
- Group Video Recording (if required)

---

## Authors

- **Shreyansh Budhia**  
- **William Brewster**  
- **Ramzi Nia**

---
## Version Control Reflection

Our team collaborated using GitHub for version control. Initial challenges included merge conflicts and inconsistent file naming across local and remote repositories. These were resolved using structured folders, frequent commits, and clear division of responsibilities. GitHub enabled transparent collaboration, version tracking, and reproducibility of our workflow.

## Course Context

This project was completed as part of a **graduate-level data analytics and public policy course**, emphasizing:
- Cross-platform validation  
- Statistical reasoning  
- Data storytelling  
- Decision-maker framing  

