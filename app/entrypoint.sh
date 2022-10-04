#!/bin/sh

python manage.py collectstatic --no-input
python manage.py createsuperuser --username tricia --email no-reply@mail.com --no-input
python manage.py migrate

exec "$@"