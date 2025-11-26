import pandas as pd
import os
import numpy as np

# -------------------------------
# Setup paths
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_DIR = os.path.join(BASE_DIR, "../dataset/processed")
file_path = os.path.join(PROCESSED_DIR, "my_sensor_data_cleaned.csv")

# -------------------------------
# Load cleaned dataset
# -------------------------------
df = pd.read_csv(file_path, parse_dates=['timestamp'])
print("Dataset loaded. First 5 rows:")
print(df.head(), "\n")

# -------------------------------
# Fault detection thresholds
# -------------------------------
# Using mean ± 2*std to catch anomalies
def detect_faults(df):
    faults = {}

    # Pressure spikes
    pressure_mean = df['pressure'].mean()
    pressure_std = df['pressure'].std()
    pressure_spikes = df[df['pressure'] > pressure_mean + 2*pressure_std]
    faults['pressure_spikes'] = pressure_spikes

    # Temperature anomalies (high or low)
    temp_mean = df['temperature'].mean()
    temp_std = df['temperature'].std()
    temp_anomalies = df[(df['temperature'] > temp_mean + 2*temp_std) |
                        (df['temperature'] < temp_mean - 2*temp_std)]
    faults['temperature_anomalies'] = temp_anomalies

    # Vibration spikes
    vibration_mean = df['vibration'].mean()
    vibration_std = df['vibration'].std()
    vibration_spikes = df[df['vibration'] > vibration_mean + 2*vibration_std]
    faults['vibration_spikes'] = vibration_spikes

    return faults

# -------------------------------
# Detect faults
# -------------------------------
faults = detect_faults(df)

# -------------------------------
# Print summary
# -------------------------------
for key, fault_df in faults.items():
    print(f"\nFault type: {key}")
    print(f"Number of occurrences: {len(fault_df)}")
    if not fault_df.empty:
        print(fault_df[['machine_id', 'timestamp', 'pressure', 'temperature', 'vibration', 'pump_rpm']].head(5))

# -------------------------------
# Save results
# -------------------------------
output_dir = os.path.join(BASE_DIR, "../tests/fault_results")
os.makedirs(output_dir, exist_ok=True)

for key, fault_df in faults.items():
    fault_file = os.path.join(output_dir, f"{key}.csv")
    fault_df.to_csv(fault_file, index=False)
    print(f"\nSaved {key} data to: {fault_file}")
