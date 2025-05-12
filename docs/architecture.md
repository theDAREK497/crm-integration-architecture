# CRM integration microservice architecture

## General Description
This document describes a microservice architecture for integrating CRM systems of Gazprom subsidiaries with the corporate portal. The architecture is developed using the [C4 Model](https://c4model.com/ ) methodology and implemented as a REST API on FastAPI.

---

## Levels of C4 Model

### **Level 1: Context Diagram**
```mermaid
graph TD
    User[User] --> CRM[CRM system]
    CRM --> Portal[Corporate Portal]
    Portal --> DB[(Database)]
    User --> Portal
    classDef service fill:#FFD700,stroke:#333;
    classDef component fill:#98FB98,stroke:#333;
    class Portal,CRM,DB service;
```
### ** Level 2: Component Diagram**
```mermaid
graph TD
    Portal --> Auth[Authentication]
    Portal --> DataSync[Data Synchronization]
    Portal --> Reporting[Report generation]
    DataSync --> CRM
    Reporting --> DB[(PostgreSQL)]
    classDef component fill:#87CEEB,stroke:#333;
    class Auth,DataSync,Reporting component;
```
Level 3: Code Structure
```mermaid
graph TD
    main.py --> routers[Routers]
    main.py --> models[Data models]
    main.py --> services[Service Logic]
    services --> db[Database]
    classDef code fill:#FFB6C1,stroke:#333;
    class routers,models,services,db code;
```

## REST API
### GET /users

Returns a list of users from the CRM system

Example response:

```bash
[
    {"id": 1, "name": "Иван Иванов", "email": "ivan@example.com"},
    {"id": 2, "name": "Мария Смирнова", "email": "maria@example.com"}
]
```
### Swagger UI

http://localhost:8000/docs

### Technology

| CATEGORY | TECHNOLOGY |
|---|---|
| Frontend | HTML5, CSS3, JavaScript, jQuery, React, Sass/SCSS |
| Backend | Python (FastAPI), PHP, C/C++ |
| DevOps | Docker, CI/CD, Linux, Zabbix, Git |
| Databases | PostgreSQL, MySQL, SQL |
| Tools | Mermaid (diagrams), UML/C4, Swagger, GitHub Actions |
| Advanced | SEO optimization, 1C-Bitrix, WordPress, Tilda, Bitrix24 API, PyTorch |

## Key Solutions
**Scalability:** Microservice architecture allows for easy addition of new modules (e.g. integration with other CRMs)
**Security:** Authentication via OAuth2 (can be added)
**Performance:** Utilization of asynchronous requests in FastAPI
**Monitoring:** Logging and metrics can be added via Prometheus (see Extension section)

## Extension
### Possible enhancements:
**1. Add PostgreSQL:
```bash
# Example of connection via SQLAlchemy
from sqlalchemy import create_engine
engine = create_engine("postgresql://user:password@localhost/dbname")
```
**2. Integration with Zabbix:**
```bash
# Add to Dockerfile
RUN apt-get update && apt-get install -y zabbix-agent
```
**3. CI/CD:**
```bash
# .github/workflows/deploy.yml
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: docker build -t crm-service .
```

## Author
**Gurikov Ilya Olegovich**
[GitHub](https://github.com/theDAREK497?spm=a2ty_o01.29997173.0.0.74b55561FmLmHM) | [LinkedIn](https://linkedin.com/in/ilion9871?spm=a2ty_o01.29997173.0.0.74b55561FmLmHM)