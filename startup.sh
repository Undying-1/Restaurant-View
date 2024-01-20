#!/bin/bash

if [ -x "$(command -v docker)" ]; then
    echo "Docker exists"
    docker-compose up --build -d
    container_name="restaurant_view"
    container_id=$(docker ps -qf "name=$container_name")

    if [ -n "$container_id" ]; then
        echo "Container ID: $container_id"
        docker exec -it "$container_id" python manage.py migrate
        docker exec -it "$container_id" python manage.py createsuperuser
    else
        echo "Container not found. Check your container name."
    fi
else
    echo "Please install docker to your system"
fi