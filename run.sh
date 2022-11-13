#! /bin/bash

##### SETUP
linebreak=$'\n'
# link=$(eval "readlink -f run.sh")
# arr=(`echo $link | tr '/' ' '`)
# echo "${#arr[@]}"
# link=${link#"/${arr[0]}"}
# link=${link#"/${arr[1]}"}
# link=${link%"/run.sh"}
# eval "cd ~$link"
# eval "cd ~/Documents/otani_proj"

##### INPUT

args=("$@")

### This is for all project
if [[ ${args[0]} == "start" ]]; then
    echo "Starting docker..."
    eval "cd backend"
    output=$(eval "docker compose up -d")
    echo "$output"
    eval "cd .."
    eval "cd frontend"
    output=$(eval "docker compose up -d")

elif [[ ${args[0]} == "stop" ]]; then
    echo "Stopping docker..."
    eval "cd backend"
    output=$(eval "docker compose down")
    echo "$output"
    eval "cd .."
    eval "cd frontend"
    output=$(eval "docker compose down")

elif [[ ${args[0]} == "createsuperuser" ]]; then
    if [[ "${args[1]}" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$ ]]
    then
        echo "Starting database..."
        eval "cd backend $linebreak docker compose up db -d"
        output=$(eval "docker compose exec backend python database/postgres/peewee/superuser.py ${args[1]}")
    else
        output="Email address ${args[1]} is invalid."
    fi

### This is for backend command
elif [[ ${args[0]} == "be" ]]; then
    eval "cd backend"
    if [[ ${args[1]} == "docker" ]]; then
        if [[ ${args[2]} == "up" ]]; then
            if [[ ${args[3]} ]]; then
                output=$(eval "docker compose up ${args[3]} -d")
            else
                output=$(eval "docker compose up -d")
            fi
        elif [[ ${args[2]} == "down" ]]; then
            if [[ ${args[3]} ]]; then
                output=$(eval "docker compose stop ${args[3]}")
            else
                output=$(eval "docker compose down")
            fi
        elif [[ ${args[2]} == "logs" ]]; then
            output=$(eval "docker compose logs ${args[3]} -f tails=50")
        elif [[ ${args[2]} == "build" ]]; then
            output=$(eval "sudo docker compose build")
        elif [[ ${args[2]} == "buildup" ]]; then
            output=$(eval "sudo docker compose up -d --build")
        else
            output="unknow command '${args[2]}'"
        fi

    elif [[ ${args[1]} == "db" ]]; then
        if [[ ${args[2]} == "migrate" ]]; then
            output=$(eval "docker compose exec backend alembic revision --autogenerate -m "migrate"")
        elif [[ ${args[2]} == "downgrate" ]]; then
            output=$(eval "docker compose exec backend alembic downgrade -1")        
        elif [[ ${args[2]} == "makemigrations" ]]; then
            output=$(eval "docker compose exec backend alembic upgrade head")
        elif [[ ${args[2]} == "rmmigrations" ]]; then
            eval "cd migrations"
            eval "sudo rm -rf versions"
            eval "sudo mkdir versions"
            output="Remove all migrations.${linebreak}Now remove 'alembic_version' table in postgres"
        else
            output="unknow command '${args[2]}'"
        fi
    
    elif [[ ${args[1]} == "sampledata" ]]; then
        echo "Starting database..."
        eval "docker compose up db -d"
        eval "cd database"
        eval "cd postgres"
        eval "cd peewee"
        echo "Creating sample data..."
        eval "python3 sample_data.py"
        output="Done"

    else
        output="unknow command '${args[1]}'"
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
            output="unknow command '${args[2]}'"
        fi
    fi

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
    output="unknow command '${args[0]}'"
fi

echo "$output"