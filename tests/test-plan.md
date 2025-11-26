# Initial Test Plan

This document describes the preliminary test strategy for the Rubber Molding IoT project.

## 1. Test Categories

1. **Unit Tests**
   - Verify individual functions and modules (e.g., simulator data generation, ingestion API endpoints).
2. **Integration Tests**
   - Check that simulator → ingestion → storage → API pipeline works end-to-end.
3. **Load / Performance Tests**
   - Simulate multiple machines sending data at target frequencies.
   - Verify ingestion latency and system stability.
4. **Acceptance Tests**
   - Trigger known fault scenarios and verify:
     - Anomaly detection triggers correctly.
     - Predictive maintenance alerts generated.
     - Dashboard updates as expected.
5. **ML Model Tests**
   - Ensure reproducible train/test splits.
   - Evaluate anomaly detection metrics (precision / recall / F1).
   - Validate predictive maintenance model outputs.

## 2. Preliminary Test Cases

| Test Case                  | Description                        | Expected Result                     | Owner  |
|-----------------------------|------------------------------------|-------------------------------------|--------|
| Simulator generates normal data | Run generator in normal mode       | JSON/CSV with valid fields          | Nishi  |
| Simulator fault injection   | Run generator in fault mode         | Fault label appears in output       | Nishi  |
| Ingestion endpoint accepts POST | Send sample JSON                  | Data stored in DB / S3              | Jeevani|
| End-to-end pipeline         | Simulator → ingestion → DB → dashboard | Dashboard reflects simulated values | Team   |

## 3. Fault Scenarios

- **Overpressure:** pressure > max_threshold
- **High temperature:** temp > max_temp
- **Vibration spike:** vibration > normal_range
- **Oil viscosity drop:** viscosity < min_value
- **Cycle time anomaly:** cycle_time too short/long

> This list will be expanded as simulator and ML models are developed.

## 4. Next Steps

- Add detailed unit test scripts for each module.
- Define integration test automation.
- Include load test scripts using multiple simulated machines.
- Document acceptance criteria for ML alerts.

Fault Scenarios for Hydraulic Rubber Molding Machine

This document outlines possible fault scenarios detected from the machine telemetry dataset. These scenarios are based on pressure, temperature, vibration, and pump speed anomalies.

1️⃣ Pressure Spikes

Description:
Sudden increases in hydraulic pressure that exceed normal operating limits.

Detection Method:

Threshold: Mean pressure + 2 × standard deviation

Look for consecutive or single extreme pressure values

Possible Causes:

Blocked valves or pipes

Overloading of the hydraulic system

Faulty pressure sensor

Implications:

Potential damage to machine components

Reduced product quality

Safety hazards

Example:

machine_id	timestamp	pressure	temperature	vibration	pump_rpm
1	2024-01-01 00:08:41	115.88	182.98	0.16	1489.97
2️⃣ Temperature Anomalies

Description:
Unexpected rises or drops in machine temperature outside normal ranges.

Detection Method:

Threshold: Mean temperature ± 2 × standard deviation

Possible Causes:

Cooling system failure or blockage

Overheating of hydraulic fluid

Sensor malfunction

Implications:

Reduced machine efficiency

Material defects due to inconsistent molding temperature

Possible safety issues

Example:

machine_id	timestamp	pressure	temperature	vibration	pump_rpm
1	2024-01-01 00:00:24	120.91	176.98	0.10	1464.09
3️⃣ Vibration Spikes

Description:
Abnormal vibration levels indicating mechanical stress or misalignment.

Detection Method:

Threshold: Mean vibration + 2 × standard deviation

Possible Causes:

Misaligned shafts or rotors

Worn bearings or components

Loose mounting of machine parts

Implications:

Accelerated wear and tear

Potential machine breakdown

Reduced product quality

Example:

machine_id	timestamp	pressure	temperature	vibration	pump_rpm
1	2024-01-01 00:12:35	119.45	180.12	0.42	1450.50
4️⃣ Increased Pump RPM

Description:
Sudden spikes in pump RPM that exceed normal operating values.

Detection Method:

Threshold: Mean pump_rpm + 2 × standard deviation

Possible Causes:

Excessive load on hydraulic system

Malfunctioning pump or control system

Feedback loop errors

Implications:

Increased energy consumption

Potential damage to pump and hydraulic circuits

Notes

Thresholds are statistical (z-score based), can be adjusted based on historical data.

Scenarios can be combined for multi-metric faults, e.g., high pressure + high temperature.

Fault detection is data-driven and helps plan predictive maintenance schedules.
