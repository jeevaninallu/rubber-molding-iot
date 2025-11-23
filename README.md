# Rubber Molding IoT Project

This project simulates IoT data from a rubber molding machine and builds 
end-to-end ingestion, analytics, anomaly detection, and predictive maintenance features.

## Project Structure
- /simulator
- /ingestion
- /backend
- /ml
- /frontend
- /infra
- /docs
- /tests

## Architecture Decision: Cloud Provider — Microsoft Azure

We have selected **Azure** as the cloud provider.

### Why Azure?
Azure has strong IoT and manufacturing-focused services:
- Azure IoT Hub for device-style telemetry
- Event Hub for high-throughput streaming
- Azure Functions for serverless processing
- Time Series Insights for telemetry visualization
- Blob Storage for raw data
- Azure ML for end-to-end model training and deployment

### Summary
Azure’s ecosystem fits industrial-style telemetry pipelines.  
Its IoT Hub + Event Hub combination supports the ingestion → processing → prediction workflow with enterprise-grade security.
