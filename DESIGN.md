# Expense Tracking Platform

## 1. Vision
Build an open-source, observability-first personal expense tracking system to learn and 
demonstrate SRE, cloud-native, and reliability engineering concepts.

This project solves a real problem: tracking expenses across multiple accounts and understanding 
where money goes, while serving as a realistic distributed system for learning Kubernetes, 
networking, observability, and incident response.

## 2. Problem Statement
At the end of the month, I can’t clearly account for:
- Where money came from
- Where it went
- What categories dominate my spending
- How transfers between accounts affect visibility

Technically, this mirrors real production challenges:
- Multiple data sources
- Ingestion delays
- Partial failures
- Data consistency
- User trust and reliability

## 3. Learning Goals
- Linux systems and processes
- Containerization with Docker
- Service networking
- Kubernetes orchestration
- Metrics with Prometheus
- Tracing with OpenTelemetry
- Logging pipelines
- SLOs, SLIs, alerting
- Incident response and postmortems

## 4. System Overview
(High-level architecture diagram will go here)

## 5. Services
- Frontend (dashboard)
- Ingestion API
- Processing/categorization service
- Storage (Postgres)
- Observability stack (Prometheus, Grafana, Loki, OTel Collector)

## 6. Observability Design
- What metrics matter
- What traces matter
- What logs matter

## 7. Reliability Scenarios
- Bank API outage
- Slow database
- Dropped transactions
- Duplicate entries
- High latency

## 8. Roadmap
### Phase 1: Local with Docker
### Phase 2: Kubernetes
### Phase 3: Observability
### Phase 4: Failure Injection & SLOs
### Phase 5: Cloud Deployment

## 9. Portfolio Outputs
- Architecture diagrams
- Dashboards
- Incident reports
- Blog posts
- Demo videos
