# Theme-Park-Ride
Building a Spring Boot application with dev/prod environments.

## Environments
This project supports two environments using Spring profiles and environment variables.

### Development (dev)
- Profile: `dev`
- H2 console: enabled
- Actuator endpoints: all exposed
- Example config: `env/dev.env`
- Default host port: `5001`

### Production (prod)
- Profile: `prod`
- H2 console: disabled
- Actuator endpoints: `health`, `info`, `prometheus`
- Example config: `env/prod.env`
- Default host port: `5000`
- Persistent data volume mounted at `/data`

## Run locally
Development:
```bash
docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d
```

Production:
```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Monitoring (Prometheus + Grafana)
Start app + monitoring stack:
```bash
docker compose \
  -f docker-compose.yml \
  -f docker-compose.dev.yml \
  -f docker-compose.monitoring.yml \
  up -d
```

Useful endpoints:
- App health: `http://localhost:5001/actuator/health`
- App Prometheus metrics: `http://localhost:5001/actuator/prometheus`
- Prometheus UI: `http://localhost:9090`
- Grafana UI: `http://localhost:3000` (default: `admin` / `admin`)

Provisioned files:
- Prometheus scrape config: `monitoring/prometheus.yml`
- Grafana datasource provisioning: `monitoring/grafana/provisioning/datasources/datasource.yml`
- Grafana dashboard provisioning: `monitoring/grafana/provisioning/dashboards/dashboard.yml`
- Example dashboard JSON: `monitoring/grafana/dashboards/theme-park-overview.json`

## Configuration sources
Common defaults live in `src/main/resources/application.yml`. Environment-specific overrides are in:
- `src/main/resources/application-dev.yml`
- `src/main/resources/application-prod.yml`

Environment variables are loaded via `env/dev.env` or `env/prod.env` in Docker Compose.

## CI/CD behavior
- Development (review) deploy runs automatically using dev profile.
- Production deploy requires manual approval in CI (`when: manual`).
