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
- Actuator endpoints: only health/info
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

Health check:
```bash
curl http://localhost:5001/actuator/health
```

## Configuration sources
Common defaults live in `src/main/resources/application.yml`. Environment-specific overrides are in:
- `src/main/resources/application-dev.yml`
- `src/main/resources/application-prod.yml`

Environment variables are loaded via `env/dev.env` or `env/prod.env` in Docker Compose.

## CI/CD behavior
- Development (review) deploy runs automatically using dev profile.
- Production deploy requires manual approval in CI (`when: manual`).
