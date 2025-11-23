# Cloud Services for Rubber Molding IoT Project

This document lists the primary cloud services recommended for the project and the role each service will play in the Week-1 → Week-12 roadmap. Architects should pick one cloud provider (AWS / GCP / Azure) and adjust the chosen services accordingly.

## Recommended Services 

### Ingestion
- **AWS:** AWS IoT Core or API Gateway + ALB (HTTP)  
**Purpose:** device-like connectivity, secure device auth, message ingestion.

### Streaming / Queue
- **AWS:** Kinesis Data Streams   
**Purpose:** durable, scalable message streaming for real-time processing.

### Stream Processing / Transform
- **AWS:** AWS Lambda (or Kinesis Data Analytics)   
**Purpose:** transform, enrich, windowing, compute rolling features.

### Time-series Storage
- **AWS:** Timestream (or InfluxDB/TimescaleDB on RDS/EC2)   
**Purpose:** fast time-series queries for dashboarding and ML feature extraction.

### Data Lake / Raw Storage
- **AWS:** S3  
**Purpose:** raw JSON/CSV storage, model training data, backups, audit logs.

### Batch / Feature Store
- **AWS:** Redshift / RDS (Postgres + Timescale) / Glue catalog  
**Purpose:** aggregated features, training datasets, long-term analytics.

### ML Training & Model Registry
- **AWS:** SageMaker + SageMaker Model Registry (or MLflow)  
**Purpose:** train, validate, version, and deploy models.

### Model Serving / Inference
- **AWS:** SageMaker endpoints or Lambda for light models   
**Purpose:** real-time scoring & batch inference jobs.

### Dashboard & Visualization
- **Grafana** (connect to Timestream/Influx/Timescale) for operator dashboards.  
- **React** frontend for custom operator/manager views; embed Grafana panels or call APIs.

### API & Authentication
- **Backend:** FastAPI (dev) → REST endpoints for telemetry/alerts/history.  
- **Auth:** Cognito (AWS) / Identity Platform (GCP) / Azure AD (Azure) + JWT.  
**Purpose:** secure operator access, role-based views, external integrations.

### CI/CD & IaC
- **IaC:** Terraform for reproducible infra provisioning.  
- **CI/CD:** GitHub Actions to lint, test, build, and deploy to dev environment.

### Cost & Monitoring
- Cost control: Budgets/alerts (AWS Budgets / GCP Budgets / Azure Cost Management)  
- Observability: CloudWatch / Stackdriver / Azure Monitor + Grafana dashboards.

---

## Notes & Decisions
- For prototyping, prefer fully managed services (SageMaker / Vertex AI) to reduce ops overhead.
- Start with a low-cost dev environment: low-frequency simulator, limited retention, and budget alerts.
- Document final cloud choice and short justification in `/docs/cloud_decision.md`.

