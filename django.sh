#!/bin/bash
echo "Waiting for the database to be ready..."
/app/wait-for-it.sh db:5432 -- echo "Database is ready!"

echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000
