# AI Chatbot
A containerized AI chat bot built with Redis caching, observability with Prometheus/Grafana and CI/CD automation with github Actions. 
The surrounding infrastructure of this project aims for production ready software that utilizes containerization, observability, automated testing, and deployment pipelines.

## Tech Stack
- **Runtime**: Python 3.10.12
- **API Framework**: FastAPI
- **LLM**: Antropic
- **Containerization**: Docker, Docker Compose
- **Monitoring**: Prometheus, Grafana
- **CI/CD**: GitHub Actions


## Features
- RESTful API endpoint for chat interactions
- Containerized deployment with Docker
- Multi-service orchestration with Docker Compose
- Prometheus metrics collection
- Grafana dashboards for visualization
- Automated testing and linting pipeline
- Environment-based configuration


## Project Status
🚧 Currently in development
- [x] **Project structure and planning**
- [x] **Core agent implementation**
        - Three-layer architecture: abstract interface, Anthropic implementation, FastAPI exposure with validation
- [x] **FastAPI REST API with validation**
- [x] **Docker containerization**
- [x] **Docker Compose orchestration**
- [x] **Redis Server side Caching**
- [x] **Prometheus and Grafana monitoring**
- [x] **GitHub Actions CI/CD pipeline**
- [ ] **Documentation and polish**


## Why I Built This
I am a platform engineer in the making. Understanding how software runs in a production environment and how to effectively deploy, monitor, scale, and maintain software fascinates me. 
I built this project to sharpen those skills. The function of the agent is okey, but from my perspective, it is secondary to the platform it is built upon.


## Getting Started
*Setup instructions will be added as the project develops.*