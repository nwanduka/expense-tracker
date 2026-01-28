# Expense Tracking Platform

## 1. Vision
Build an open-source, observability-first personal expense tracking system to learn and 
demonstrate SRE, cloud-native, and reliability engineering concepts.

This project solves a real problem: tracking expenses across multiple accounts and understanding 
where money goes, while serving as a realistic distributed system for learning Kubernetes, 
networking, observability, and incident response.

## 2. Problem Statement
- I lose track of where my money goes every month.
- I have multiple bank accounts and apps, making it hard to know the total inflow/outflow.
- I want to understand spending patterns and spot unusual expenses.

## 3. Goals
- Build a simple, usable expense tracker.
- Learn cloud-native tooling: Docker, Linux, Prometheus, OpenTelemetry, etc.
- Design with observability-first principles.
- Make it open source so others can use it for free.

## 4. High-Level Architecture
- Frontend: Web UI / CLI interface (v0.1)
- Backend: API service to record transactions
- Database: Store transactions, categories, accounts
- Observability: Prometheus metrics, OpenTelemetry traces/logs
- Deployment: Docker initially, then Kubernetes for orchestration

## 5. Features
- Log income and expenses with categories and accounts.
- Summarize monthly spending.
- Query/filter transactions.
- Track trends over time.
- Optional: alerts for unusual transactions (stretch goal).

## 6. Reliability Scenarios
- Bank API outage
- Slow database
- Dropped transactions
- Duplicate entries
- High latency

## 7. Roadmap
| Version	| Focus |
| ------- | ----- |
| v0.1	| CLI expense logging + storage |
v0.2 | Web UI + basic charts
v0.3	| API + structured logs
v0.4	| Metrics + traces integration
v0.5	| Dockerized deployment
v0.6	| Kubernetes deployment + dashboards
v0.7	| CI/CD + automated tests
v0.8	| Contributor-friendly documentation & guides
