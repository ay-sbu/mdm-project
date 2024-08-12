#!/bin/bash

echo "collect static files"
python manage.py collectstatic --noinput

echo "migration"
python manage.py makemigrations
python manage.py migrate

uvicorn config.asgi:application --port 8000 --workers 4 --log-level debug --reload