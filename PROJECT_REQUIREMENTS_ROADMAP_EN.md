# Project Requirements Roadmap (EN)

This document evaluates the current repository against the provided **Project Requirements & Expectations** and provides a practical action roadmap.

## 1) Dockerize Your Application
**Status:** ✅ Mostly complete.
- A multi-stage `Dockerfile` exists (build + runtime).
- Docker Compose run flow exists.
- There is evidence of registry usage (GitLab registry image reference).

**Improve:**
- Make image push in CI explicit and documented.

## 2) Multiple Environments (Dev & Prod)
**Status:** ✅ Complete.
- Separate compose overrides: `docker-compose.dev.yml` and `docker-compose.prod.yml`.
- Separate env files: `env/dev.env` and `env/prod.env`.
- CI flow supports auto dev deploy + manual approval for prod.

## 3) Testing
**Status:** ⚠️ Partially complete.
- Unit/API-style tests exist with Spring Boot test + MockMvc.
- Jenkins pipeline runs `./gradlew test`.

**Missing / Improve:**
- Add coverage reporting (e.g., JaCoCo).
- Add at least one stronger layer (integration/API contract/E2E) to improve confidence.

## 4) Kubernetes Orchestration
**Status:** ✅ Complete (via Helm chart).
- Deployment/Service/Ingress templates are present.

**Missing / Improve:**
- ConfigMap/Secret templates are not clearly present.
- Clearly document dev/prod namespace strategy.

## 5) CI/CD Pipeline
**Status:** ✅ Complete.
- Jenkins pipeline includes build, test, Docker build, deploy stages.
- Prod deployment is approval-gated.

**Improve:**
- Document branching/release strategy.
- Keep image push + K8s deploy path consistent in one clear pipeline flow.

## 6) Monitoring (Prometheus + Grafana / Datadog)
**Status:** ✅ Complete (via Docker Compose monitoring stack).
- `docker-compose.monitoring.yml` defines both Prometheus (`9090`) and Grafana (`3000`) services.
- Grafana admin credentials are defined in compose (`admin/admin`).
- Prometheus scrape config and Grafana datasource/dashboard provisioning files are present in the repository.

### How to Use Prometheus and Grafana (Quick Guide)
1. Start the monitoring stack:
   - `cd theme-park-ride-gradle`
   - `docker compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d`
2. Verify the application metrics endpoint:
   - `http://localhost:5001/actuator/prometheus`
3. Open Prometheus UI:
   - `http://localhost:9090`
   - Run `up` in the **Expression** box and click **Execute** to verify targets are healthy.
4. Open Grafana UI:
   - `http://localhost:3000`
   - Login with `admin` / `admin` (Grafana may request a password change on first login).
5. Use dashboards in Grafana:
   - Open **Dashboards** from the left menu.
   - Open the provisioned dashboard (e.g., `theme-park-overview`).
   - Change time range (last 5m / 1h) and inspect metric trends.
6. Common Prometheus queries (examples):
   - `up`
   - `rate(http_server_requests_seconds_count[5m])`
   - `jvm_memory_used_bytes`

## 7) Security (DevSecOps)
**Status:** ⚠️ Partially complete.
- CI credentials usage is present.

**Missing:**
Implement at least 3 security controls explicitly, such as:
1. Container image scanning (Trivy)
2. Dependency scanning (Dependabot/Snyk)
3. Secrets management (K8s Secret + external secret store)
4. HTTPS ingress + cert-manager
5. (Bonus) RBAC

## 8) Disaster Recovery
**Status:** ❌ Missing.
- Backup/restore process and rollback runbooks are not clearly documented.

## 9) Documentation + Architecture Diagram
**Status:** ⚠️ Partially complete.
- READMEs exist.
- Full required sections (monitoring, security, DR, architecture diagram) are not yet complete in one coherent location.

---

## Should Terraform be added?
**Short answer:** Not strictly mandatory in this requirement list, but **strongly recommended**.

You can satisfy deployment with Kubernetes manifests/Helm, but Terraform significantly improves the "redeploy infrastructure from IaC" expectation and production realism.

**Good Terraform scope candidates:**
- Network + cluster provisioning
- Registry/IAM/policy resources
- Monitoring base infrastructure

---

## Practical 2-Week Roadmap
1. **Productionize monitoring first:** keep the existing compose monitoring stack and extend it to Kubernetes (kube-prometheus-stack/Helm), including at least 1 alert rule.
2. **Security hardening:** add Trivy scan in CI, enable dependency scanning, migrate secrets to proper secret handling.
3. **DR runbook:** document backup/restore + rollback scenarios.
4. **K8s completeness:** add ConfigMap/Secret templates and namespace strategy.
5. **Terraform baseline:** add minimum infra modules (cluster/namespace/registry).
6. **Documentation unification:** collect dev/prod, CI/CD, monitoring, security, DR, and architecture in the main docs.

---

## "Is everything complete?"
With the current repository state: **Partially complete, with remaining gaps.**
Monitoring is complete at Docker Compose level; main gaps are DR and explicit implementation evidence for at least 3 security controls.
