#Exploratory Data Analysis (EDA) Report
Dataset Overview

Total entries: 1973

Features: 6

machine_id (int)

timestamp (datetime)

pressure (float)

temperature (float)

vibration (float)

pump_rpm (float)

#No missing values in any column.

Missing Values Report
Column	Missing Values
machine_id	0
timestamp	0
pressure	0
temperature	0
vibration	0
pump_rpm	0

#Correlation Analysis

Correlation heatmap indicates that all numeric features are weakly correlated.

Correlation coefficients:

pressure vs temperature: 0.02

pressure vs vibration: 0.00

pressure vs pump_rpm: -0.05

temperature vs vibration: 0.02

temperature vs pump_rpm: -0.03

vibration vs pump_rpm: 0.01

Insight: Features are mostly independent, which is good for multivariate analysis.

Fault vs Normal Patterns

No missing values or extreme outliers detected after cleaning.

Outliers removed using z-score method: 1973 rows remain from original 2000.

This cleaned dataset can now be used to identify fault patterns for machine operations.

##############Summary##########33

Dataset is clean and ready for ML modeling.

No missing values; timestamps standardized.

Features are mostly independent; EDA suggests using all numeric features for predictive modeling.

Next step: Identify fault scenarios and classify anomalies using ML models.