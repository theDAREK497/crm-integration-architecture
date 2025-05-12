# CRM Integration Architecture

Example of microservice architecture implementation for integrating CRM systems with web platforms.  
Includes C4 Model diagrams, REST API (FastAPI) and Docker containerization.

## Technologies
- **FastAPI** - for REST API creation
- **Mermaid** - for C4 Model diagrams
- **Docker** - for containerization
- **Python 3.13** - programming language

## Installation and startup

### 1. Clone the repository
```bash
git clone https://github.com/ your-name/crm-integration-architecture.git
cd crm-integration-architecture
```
### 2. Build the Docker image
```bash
docker build -t crm-service .
```
### 3. Start the container
```bash
docker run -p 8000:8000 crm-service
```
### 4. Open the Swagger documentation
http://localhost:8000/docs

### Architecture
See the diagrams under docs/architecture.md

## License
MIT License


#### **docs/architecture.md**

## Architecture Description

### C4 Model Levels
1. **Level 1 (Context)**: Interaction between user, CRM system, and enterprise portal.
2. **Level 2 (Components)**: Service modules (authentication, data synchronization, reports).
3. **Level 3 (Code Structure)**: Routers, data models, and service logic.

### REST API.
- **GET /users**: Returns a list of users.
- **GET /docs**: Swagger documentation.
