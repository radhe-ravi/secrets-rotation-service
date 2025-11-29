# Secrets Rotation Service

A unified FastAPI-based microservice to fetch, cache, audit, and rotate secrets across:

- AWS Secrets Manager
- GCP Secret Manager
- Azure Key Vault
- Hashicorp Vault (future)

## Core Features

- Single `/get-secret/{env}/{service}` API
- Redis caching layer
- MongoDB audit logging
- Celery-based secret rotation workflows
- Multi-cloud provider adapters
- JWT authentication + service-to-service auth
- Zero-downtime rotations

## Project Structure

See `/app` for service code, `/infra` for deployment configs,
and `/docs` for architecture diagrams.

## Status

Phase 1: Repository structure initialization.
