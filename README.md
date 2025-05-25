# 🚧 Analysis of PMGSY Scheme (Pradhan Mantri Gram Sadak Yojana)

This repository presents an analysis of the **Pradhan Mantri Gram Sadak Yojana (PMGSY)** scheme using publicly available data. The objective is to understand the distribution, progress, and expenditure on rural road development across various Indian states.

---

## 📚 Table of Contents

- [Introduction](#Introduction)
- [Setup](#Setup)
- [Data Description](#Data_Description)
- [Analysis Steps](#Analysis_Steps)
- [Results](#Results)
- [Conclusion](#Conclusion)

---

## 🛣️ Introduction

The **PMGSY** scheme was launched to provide **all-weather road connectivity** to unconnected rural habitations. This analysis focuses on:

- Sanctioned vs. completed road works  
- Expenditure per kilometer  
- Balance road lengths  
- Scheme-wise and state-wise performance  

---

## ⚙️ Setup

- To run the analysis(Analysis_of_pmgsy.py), ensure you have the following Python libraries installed on your system:

```bash
pip install pandas numpy matplotlib
```
- Or a Google Colab Environment(PMGSY-Scheme_Analysis.ipynb)
---

## 📁 Data Description
The dataset includes the following columns:

```
STATE_NAME: Name of the state

DISTRICT_NAME: Name of the district

PMGSY_SCHEME: Scheme type under PMGSY

NO_OF_ROAD_WORK_SANCTIONED: Number of works sanctioned

NO_OF_ROAD_WORKS_COMPLETED: Number of works completed

NO_OF_ROAD_WORKS_BALANCE: Remaining road works

LENGTH_OF_ROAD_WORK_SANCTIONED_KM: Sanctioned road length (km)

COST_OF_WORKS_SANCTIONED_LAKHS: Sanctioned cost (₹ Lakhs)

LENGTH_OF_ROAD_WORK_COMPLETED_KM: Completed road length (km)

EXPENDITURE_OCCURED_LAKHS: Actual expenditure (₹ Lakhs)

LENGTH_OF_ROAD_WORK_BALANCE_KM: Balance road length (km)
```

---

## 📊 Analysis Steps

Data Cleaning:
Removed non-road columns (e.g., bridges), filtered zero or missing values.

Expenditure Metrics:

Calculated expenditure per km (sanctioned and actual).

Removed anomalies (e.g., 0 km or 0 cost rows).

State-wise & Scheme-wise Summary:
Grouped data by state and scheme to summarize:

Total sanctioned & completed works

Road lengths

Expenditure per scheme

Visualizations:

Bar plots: Completed lengths by state

Pie charts: Expenditure distribution by scheme

Histograms: Frequency of works

Balance road lengths: Per-state summary

---

## 📈 Results
Total constructions analyzed: 2245

Top 3 States by number of works:

Uttar Pradesh

Madhya Pradesh

Rajasthan

Notable insights:

Some states show high expenditure per km but lower completion rates.

PMGSY-I dominates in number of works and completion percentage.

---

## ✅ Conclusion
This analysis sheds light on the progress and efficiency of rural road development under the PMGSY scheme. It identifies top-performing states, budget utilization patterns, and areas with significant balance work, supporting future policy decisions and resource allocation.
