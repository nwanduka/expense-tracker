# expense-tracker
A personal, open-source expense tracking system built to understand spending, track multiple accounts, and practice cloud-native engineering and observability.

## The Problem

I often lose track of where my money goes each month. With multiple bank accounts, apps, and frequent transfers, it’s hard to know my total inflows, outflows, and spending patterns.

This project aims to solve that problem while giving me a sandbox to learn cloud-native tools, observability, and site reliability engineering.

## The Vision

Build a self-hostable, open-source personal finance platform that:

1. Automatically ingests transactions from my banks (via SMS/email alerts, statement uploads, and eventually API integrations)
2. Aggregates spending across multiple accounts and sources
3. Categorizes and analyzes expenses to provide actionable insights

## Current Status

🚧 **Early Development** - This project is in its infancy. I'm learning to code while building this, and I'm building in public.

**What exists now:**
- Project vision and architecture planning
- Initial repository structure

**What's coming next:**
- [x] Basic transaction storage and retrieval API
- [ ] Simple web interface for manual transaction entry
- [x] Docker containerization
- [x] Observability implementation
- [ ] Kubernetes deployment configuration
- [ ] Transaction categorization engine
- [x] Email alert parsing for major Nigerian banks
- [ ] Dashboard with spending analytics

## Architecture

The system is being built as a microservices architecture to enable:

- Independent scaling of different components
- Plugin-based extensibility for new banks and data sources
- Comprehensive observability at every layer

**Planned services:**
- **Ingestion Service**: Pulls transactions from multiple sources (SMS, email, API, uploads)
- **Deduplication Service**: Identifies and removes duplicate transactions across sources
- **Categorization Service**: Tags and categorizes expenses
- **Reconciliation Service**: Ensures data accuracy and balance matching
- **Analytics Service**: Generates insights and reports
- **API Gateway**: Unified interface for frontend
- **Web Frontend**: User interface for viewing and managing finances

**Infrastructure & Observability:**
- Containerization: Docker
- Orchestration: Kubernetes
- Metrics: Prometheus + OpenTelemetry
- Visualization: Grafana
- Database: PostgreSQL (subject to change)

## License

MIT License - see LICENSE file for details.

This means you're free to use, modify, and distribute this software, even for commercial purposes.
