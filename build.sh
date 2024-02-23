#!/usr/bin/env bash
set -o errexit

pipenv install --ignore-pipfile

python manage.py collectstatic --no-input

python manage.py makemigrations --settings=backendAPI.production_settings

python manage.py migrate --settings=backendAPI.production_settings