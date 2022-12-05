#!/bin/bash

python manage.py collectstatic --noinput &
python manage.py migrate &
python manage.py runserver 0.0.0.0:7000 &
celery -A config worker --loglevel=INFO