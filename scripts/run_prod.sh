#!/bin/bash

python manage.py collectstatic --noinput &
python manage.py migrate &
gunicorn config.wsgi:application --timeout=40 --bind 0.0.0.0:7000
