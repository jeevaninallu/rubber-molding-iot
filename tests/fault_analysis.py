import pandas as pd

df = pd.read_csv("dataset/processed/my_sensor_data_cleaned.csv")

# Example: pressure spikes
pressure_mean = df['pressure'].mean()
pressure_std = df['pressure'].std()
spikes = df[df['pressure'] > pressure_mean + 3*pressure_std]
print(spikes.head())

# Example: temperature anomalies
temp_mean = df['temperature'].mean()
temp_std = df['temperature'].std()
temp_anomalies = df[(df['temperature'] > temp_mean + 3*temp_std) | (df['temperature'] < temp_mean - 3*temp_std)]
print(temp_anomalies.head())
