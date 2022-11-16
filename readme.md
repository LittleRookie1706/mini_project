# Ta Minh Khoi(Little Rookie)'s miniproject
## Idea and Design
[Idea and Design](https://drive.google.com/file/d/189M2A2INygW1483EUw-OhHiU7SS43T_X/view)


## Port
```bash
# Web services:
    # 80: nginx: Reverse proxy
    81: nginx proxy manager: Reverse proxy with friendly interface
    3001: uptime kuma: Watching run time of services

# Frontend
    3000: frontend : Vue.js 

# Backend
    8000: backend : FastAPI 
    5050: pgadmin : Manage and visualize database 
        Default user: pgadmin4@pgadmin.org
        Default password: admin

        Register server: 
            -host: db
            -username: postgres
            -password: postgres
# Databasee
    5432: postgres : SQL database
    6379: redis : Cache
    7700: meilisearch : Fast search engine
```
## Bash script: ./run.sh + command
```bash
### Project
Run project: up
Stop project: down
Create super user: createsuperuser + email

### Backend
Backend commands: Docker & database migration
    Docker: be + docker + ( up | down | build | buildup )
    Migration: be + db + ( 
        migrate: migrate database
        downgrate: downgrade 
        makemigrations: make migrations
        resetmigrations: delete all migrations and create new one
        sampledata: create sample data
    )
    *After ``migrate`` you must ``makemigrations`` if you want to migrate next one

### Frontend
Frontend commands: 
    fe + docker( up | down | build | buildup )

### Other module
# Install services: install + service_name
See all active ports: active-port
Kill a port: kill + port_number

Example: ./run.sh be db makemigrations
```