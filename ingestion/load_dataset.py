import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  #
RAW_DIR = os.path.join(BASE_DIR, "../dataset/raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "../dataset/processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)  

filename = "my_sensor_data.xlsx"
file_path = os.path.join(RAW_DIR, filename)

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()


df = pd.read_excel(file_path)
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
