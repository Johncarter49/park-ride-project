# Theme Park Ride Service DevOps Project Overview

## Slide 1 — Title
- Theme Park Ride Service DevOps Project Overview
- English Project Presentation
- Spring Boot • Docker • CI/CD • Monitoring

## Slide 2 — Project Purpose & Scope
- Build a reliable backend service for theme park ride management.
- Demonstrate a full DevOps lifecycle: build, package, deploy, observe.
- Support environment-aware deployment with clear dev/prod separation.

## Slide 3 — Technology Stack
- Java + Spring Boot (REST API + Actuator metrics).
- Gradle build system for compilation, tests, and packaging.
- Docker + Docker Compose for local and environment-specific runtime.
- Prometheus + Grafana for metrics collection and visualization.
- Jenkins pipeline and Helm chart artifacts for CI/CD and Kubernetes deployment.

## Slide 4 — Application Architecture
- Layered Spring Boot structure.
- Controller layer exposes ride management endpoints.
- Model and repository manage ride data persistence.
- Configuration profiles tune behavior per environment.
- Actuator endpoints provide health checks and Prometheus metrics.

## Slide 5 — Environment Strategy (Dev vs Prod)
- Development profile (dev): H2 console enabled, all actuator endpoints, port 5001.
- Production profile (prod): H2 console disabled, limited actuator endpoints, port 5000.
- Production data persists using mounted volume at /data.

## Slide 6 — Containerization & Local Run
- Single base docker-compose.yml with environment-specific overrides.
- Development run: docker-compose + docker-compose.dev.yml.
- Production run: docker-compose + docker-compose.prod.yml.
- Environment variables loaded from env/dev.env and env/prod.env.

## Slide 7 — Observability & Monitoring
- Monitoring stack includes Prometheus and Grafana.
- Service health endpoint: /actuator/health.
- Metrics endpoint: /actuator/prometheus.
- Prometheus UI: localhost:9090, Grafana UI: localhost:3000.

## Slide 8 — CI/CD Pipeline & Release Flow
- Development (review) deployment runs automatically.
- Production deployment requires manual approval.
- Pipeline artifacts support Helm-based Kubernetes deployment.
- Approach balances speed in dev and control in prod.

## Slide 9 — Security & Operational Practices
- Sensitive and debug endpoints are restricted in production profile.
- Separate environment variable files for dev and prod.
- Persistent storage prevents data loss on restart.
- Health and metrics support proactive incident response.

## Slide 10 — Roadmap / Next Improvements
- Add integration and contract tests.
- Introduce secret management (Vault/KMS).
- Harden API with authentication and rate limiting.
- Expand dashboard KPIs (error rate, latency percentile, saturation).

## Slide 11 — Conclusion
- Project demonstrates practical DevOps readiness around a Spring service.
- Delivers consistent deployment, visibility, and operational control.
- Ready to scale with additional automation and production hardening.
- Thank you! Questions?
