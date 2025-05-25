# Analysis_PMGSY

Analysis of PMGSY Scheme
This repository contains an analysis of the Pradhan Mantri Gram Sadak Yojana (PMGSY) scheme using a dataset of road works and expenditures across various states in India.

Table of Contents
Introduction
Setup
Data
Analysis
Results
Conclusion
Introduction
The PMGSY scheme aims to provide all-weather road connectivity to unconnected habitations in rural areas. This analysis explores the sanctioned and completed road works, expenditure per kilometer, and other relevant metrics across different states.

Setup
To run the analysis, ensure you have the following dependencies installed:
pandas
numpy
matplotlib

```pip install pandas numpy matplotlib ```

Data
The dataset consists of the following columns:

`STATE_NAME`
`DISTRICT_NAME`
`PMGSY_SCHEME`
`NO_OF_ROAD_WORK_SANCTIONED`
`NO_OF_ROAD_WORKS_COMPLETED`
`NO_OF_ROAD_WORKS_BALANCE`
`LENGTH_OF_ROAD_WORK_SANCTIONED_KM`
`COST_OF_WORKS_SANCTIONED_LAKHS`
`LENGTH_OF_ROAD_WORK_COMPLETED_KM`
`EXPENDITURE_OCCURED_LAKHS`
`LENGTH_OF_ROAD_WORK_BALANCE_KM`
Analysis
Data Cleaning: Dropped columns related to bridges as they are not part of this analysis.
Expenditure Calculations:
Calculated the expenditure per kilometer sanctioned and actual expenditure per kilometer.
Filtered out rows with zero values in key columns.
Frequency Distribution: Analyzed the frequency distribution of road works across different states.
State and Scheme Summary: Grouped data by state and scheme, and plotted the total road lengths completed.
Expenditure Distribution: Visualized the expenditure distribution using pie charts for different schemes and states.
Balance Road Length: Summarized and plotted the balance road length by state.
Results
The analysis covers a total of 2245 constructions across the country.
The top three states with the most constructions are Uttar Pradesh, Madhya Pradesh, and Rajasthan.
Conclusion
This analysis provides insights into the progress and expenditure of the PMGSY scheme. The visualizations highlight the distribution of road works and expenditures across different states and schemes.
