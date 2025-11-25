print("Script is running")
import pandas as pd
import os

RAW_DIR = "../dataset/raw"
PROCESSED_DIR = "../dataset/processed"

filename = "my_sensor_data.xlsx"
file_path = os.path.join(RAW_DIR, filename)

# Read Excel
df = pd.read_excel(file_path)

# Quick check
print(df.head())
print(df.info())
