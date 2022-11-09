#! /bin/bash

#setup
linebreak=$'\n'

# input
args=("$@")

### This is for all project
if [[ ${args[0]} == "start" ]]; then
    eval "cd backend"
    output=$(eval "docker compose up -d")
    echo "$output"
    eval "cd .."
    eval "cd frontend"
    echo "Running docker in frontend..."
    output=$(eval "docker compose up -d")

elif [[ ${args[0]} == "stop" ]]; then
    eval "cd backend"
    output=$(eval "docker compose down")
    echo "$output"
    eval "cd .."
    eval "cd frontend"
    output=$(eval "docker compose down")

### This is for backend command
elif [[ ${args[0]} == "be" ]]; then
    eval "cd backend"
    if [[ ${args[1]} == "docker" ]]; then
        if [[ ${args[2]} == "up" ]]; then
            output=$(eval "docker compose up -d")
        elif [[ ${args[2]} == "down" ]]; then
            output=$(eval "docker compose down")
        elif [[ ${args[2]} == "logs" ]]; then
            output=$(eval "docker compose logs ${args[3]} -f tails=50")
        elif [[ ${args[2]} == "build" ]]; then
            output=$(eval "sudo docker compose build")
        elif [[ ${args[2]} == "buildup" ]]; then
            output=$(eval "sudo docker compose up -d --build")
        else
            output="unknow command ${args[2]}"
        fi

    elif [[ ${args[1]} == "db" ]]; then
        if [[ ${args[2]} == "migrate" ]]; then
            output=$(eval "docker compose exec web alembic revision --autogenerate -m "migrate"")
        elif [[ ${args[2]} == "downgrate" ]]; then
            output=$(eval "docker compose exec web alembic downgrade -1")        
        elif [[ ${args[2]} == "makemigrations" ]]; then
            output=$(eval "docker compose exec web alembic upgrade head")
        else
            output="unknow command ${args[2]}"
        fi

    else
        output="unknow command ${args[1]}"
    fi

### This is for frontend command
elif [[ ${args[0]} == "fe" ]]; then
    eval "cd frontend"
    if [[ ${args[1]} == "docker" ]]; then
        if [[ ${args[2]} == "up" ]]; then
            output=$(eval "docker compose up -d")
        elif [[ ${args[2]} == "down" ]]; then
            output=$(eval "docker compose down")
        elif [[ ${args[2]} == "logs" ]]; then
            output=$(eval "docker compose logs ${args[3]} -f tails=50")
        elif [[ ${args[2]} == "build" ]]; then
            output=$(eval "sudo docker compose build")
        elif [[ ${args[2]} == "buildup" ]]; then
            output=$(eval "sudo docker compose up -d --build")
        else
            output="unknow command ${args[2]}"
        fi
    fi

# elif [[ ${args[0]} == "env" ]]; then
#     eval "source env/bin/activate"



### This is for other tools/modules

# see all active port
elif [[ ${args[0]} == "aport" ]]; then
    output=$(eval "sudo lsof -i -P -n | grep LISTEN")

# kill active port
elif [[ ${args[0]} == "kill" ]]; then
    if [[ ${args[1]} ]]; then
        output=$(eval "sudo kill -9 $(sudo lsof -t -i:${args[1]})")
    else
        output=$"Please confirm port to kill.${linebreak}Example: 'kill 8000'"
    fi

else
    output="unknow command ${args[0]}"
fi

echo "$output"