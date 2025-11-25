import pandas as pd
import os

# -------------------- Directories --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Current script directory
RAW_DIR = os.path.join(BASE_DIR, "../dataset/raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "../dataset/processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)  # Create processed folder if not exists

# -------------------- Dataset File --------------------
filename = "my_sensor_data.xlsx"
file_path = os.path.join(RAW_DIR, filename)

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# -------------------- Read Dataset --------------------
df = pd.read_excel(file_path)
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())

# -------------------- Schema Validation --------------------
required_columns = ["timestamp", "pressure", "temperature", "vibration", "machine_id", "pump_rpm"]

# Check for missing columns
missing_cols = [col for col in required_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns: {missing_cols}")

# Convert data types
df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce')
df["pressure"] = pd.to_numeric(df["pressure"], errors='coerce')
df["temperature"] = pd.to_numeric(df["temperature"], errors='coerce')
df["vibration"] = pd.to_numeric(df["vibration"], errors='coerce')
df["pump_rpm"] = pd.to_numeric(df["pump_rpm"], errors='coerce')
df["machine_id"] = df["machine_id"].astype(str)

# -------------------- Handle Missing Values --------------------
# Fill numeric missing values with column mean
numeric_cols = ["pressure", "temperature", "vibration", "pump_rpm"]
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Optional: drop rows if timestamp or machine_id missing
df.dropna(subset=["timestamp", "machine_id"], inplace=True)

# -------------------- Remove Outliers (IQR Method) --------------------
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)

# -------------------- Standardize Timestamps --------------------
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

# -------------------- Save Cleaned Dataset --------------------
processed_file = os.path.join(PROCESSED_DIR, "cleaned_sensor_data.csv")
df.to_csv(processed_file, index=False)
print(f"\nCleaned dataset saved to: {processed_file}")