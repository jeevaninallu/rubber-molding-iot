import pandas as pd
import os

# -------------------------------
# Setup paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of this script
RAW_DIR = os.path.join(BASE_DIR, "../dataset/raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "../dataset/processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)  # create folder if not exists

filename = "my_sensor_data.xlsx"
file_path = os.path.join(RAW_DIR, filename)

# -------------------------------
# Debug check
# -------------------------------
print("Script is running...")
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# -------------------------------
# Read Excel
# -------------------------------
df = pd.read_excel(file_path)
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())

# -------------------------------
# Validate columns
# -------------------------------
expected_columns = ["timestamp", "pressure", "temperature", "cycle_time", "valve_position"]
for col in expected_columns:
    if col not in df.columns:
        raise ValueError(f"Missing expected column: {col}")

# -------------------------------
# Clean missing values
# -------------------------------
df = df.dropna()  # remove rows with any missing value
print(f"\nRows after dropping missing values: {len(df)}")

# -------------------------------
# Remove outliers (example: z-score method)
# -------------------------------
from scipy import stats
import numpy as np

numeric_cols = ["pressure", "temperature", "cycle_time", "valve_position"]
df = df[(np.abs(stats.zscore(df[numeric_cols])) < 3).all(axis=1)]
print(f"Rows after removing outliers: {len(df)}")

# -------------------------------
# Standardize timestamp
# -------------------------------
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")
print("Timestamps standardized.")

# -------------------------------
# Save cleaned data
# -------------------------------
processed_file = os.path.join(PROCESSED_DIR, "my_sensor_data_cleaned.csv")
df.to_csv(processed_file, index=False)
print(f"Cleaned data saved to: {processed_file}")


import boto3
import os

def upload_to_s3(local_file_path, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"Uploaded to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print("Upload failed:", e)

