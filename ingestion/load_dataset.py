import pandas as pd
import os

print("Script is running...")  # Debug line

RAW_DIR = "../dataset/raw"
PROCESSED_DIR = "../dataset/processed"

filename = "my_sensor_data.xlsx"
file_path = os.path.join(RAW_DIR, filename)

# Check if file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Read Excel
    df = pd.read_excel(file_path)

    # Quick check
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset info:")
    print(df.info())
