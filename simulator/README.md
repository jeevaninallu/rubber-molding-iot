# Simulator Module

This module simulates IoT data from rubber molding machines.  
It generates telemetry streams including machine parameters and fault scenarios for testing ingestion, analytics, and anomaly detection pipelines.

## Purpose

- Provide realistic machine telemetry in **JSON** or **CSV** format.
- Include both **normal** and **faulty** operating conditions.
- Serve as the data source for ingestion, dashboards, and ML pipelines.

## Files

- `__init__.py` — marks this as a Python package.
- `config.py` — configuration parameters (frequency, number of machines, fault injection settings).
- `data_generator.py` — main script for generating simulated data.
- `README.md` — this file.

## Dependencies

- Python 3.9+
- pandas
- numpy
- paho-mqtt (optional, for MQTT output)
- fastapi (optional, for local ingestion testing)

Install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

