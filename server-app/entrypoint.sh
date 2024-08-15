#!/bin/bash

echo "collect static files"
python manage.py collectstatic --noinput

echo "migration"
python manage.py makemigrations
python manage.py migrate

exec "$@"