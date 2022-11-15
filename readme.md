# Ta Minh Khoi(Little Rookie)'s miniproject
## Idea and Design
[Idea and Design](https://drive.google.com/file/d/189M2A2INygW1483EUw-OhHiU7SS43T_X/view)


## Port
```bash
8000: web
5050: pgadmin
5432: postgres
6379: redis
7070: meilisearch
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
    Docker: be + docker + ( up | down | build | buildup | resetmigrations )
### Frontend
Frontend commands: 
    fe + docker( up | down | build | buildup )
### Other module
See all active ports: active-port
Kill a port: kill + port_number

Example: ./run.sh be db makemigrations
```