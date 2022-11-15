# Ta Minh Khoi(Little Rookie)'s miniproject
## Idea and Design
[Idea and Design](https://drive.google.com/file/d/189M2A2INygW1483EUw-OhHiU7SS43T_X/view)


## Port
```bash
# 80: nginx
# 81: nginx proxy manager
3000: frontend
8000: backend
5050: pgadmin
5432: postgres
6379: redis
7700: meilisearch
```

## Pgadmin
```bash
Default user: pgadmin4@pgadmin.org
Default password: admin

Register server: 
    -host: db
    -username: postgres
    -password: postgres
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
See all active ports: active-port
Kill a port: kill + port_number

Example: ./run.sh be db makemigrations
```