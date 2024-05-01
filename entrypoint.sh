#!/bin/bash

echo "Migrating the Database"
/.venv/bin/
python manage.py makemigrations --noinput
/.venv/bin/
python manage.py migrate --noinput

echo "Collecting the static files"
/.venv/bin/
python manage.py collectstatic

echo "Statrting the Server"
/.venv/bin/
gunicorn core.wsgi:application --bind 0.0.0.0:8000

