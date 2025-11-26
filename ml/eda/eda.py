# ml/eda/eda.ipynb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# Setup paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of this script
PROCESSED_DIR = os.path.join(BASE_DIR, "../../dataset/processed")
file_path = os.path.join(PROCESSED_DIR, "my_sensor_data_cleaned.csv")

# -------------------------------
# Read dataset
# -------------------------------
df = pd.read_csv(file_path, parse_dates=["timestamp"])
print("Dataset loaded. First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())

# -------------------------------
# Missing values report
# -------------------------------
missing_report = df.isnull().sum()
print("\nMissing Values Report:")
print(missing_report)

# Save missing values report to CSV
missing_report.to_csv(os.path.join(BASE_DIR, "missing_values_report.csv"))

# -------------------------------
# Correlation heatmap
# -------------------------------
numeric_cols = ["pressure", "temperature", "vibration", "pump_rpm"]
corr = df[numeric_cols].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "correlation_heatmap.png"))
plt.show()

# -------------------------------
# Fault vs Normal Distribution
# -------------------------------
# Example: define simple thresholds for faults (can be adjusted)
pressure_fault = df["pressure"] > 150
temperature_fault = df["temperature"] > 200
vibration_fault = df["vibration"] > 1.0  # hypothetical threshold
pump_rpm_fault = df["pump_rpm"] > 2000   # hypothetical threshold

df["fault"] = pressure_fault | temperature_fault | vibration_fault | pump_rpm_fault

plt.figure(figsize=(6,4))
sns.countplot(x="fault", data=df)
plt.title("Fault vs Normal Distribution")
plt.xlabel("Fault (True=Faulty, False=Normal)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "fault_vs_normal_distribution.png"))
plt.show()

# -------------------------------
# Summary statistics
# -------------------------------
summary_stats = df.describe()
print("\nSummary statistics:")
print(summary_stats)

# Save summary statistics to CSV
summary_stats.to_csv(os.path.join(BASE_DIR, "eda_summary_statistics.csv"))

# -------------------------------
# Save EDA report in Markdown
# -------------------------------
report_md = os.path.join(BASE_DIR, "eda_report.md")
with open(report_md, "w") as f:
    f.write("# EDA Report\n\n")
    f.write("## Missing Values Report\n")
    f.write(missing_report.to_markdown() + "\n\n")
    f.write("## Summary Statistics\n")
    f.write(summary_stats.to_markdown() + "\n\n")
    f.write("## Correlation Heatmap\n")
    f.write("See correlation_heatmap.png\n\n")
    f.write("## Fault vs Normal Distribution\n")
    f.write("See fault_vs_normal_distribution.png\n")
