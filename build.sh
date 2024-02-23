#!/usr/bin/env bash
set -o errexit

pipenv install --ignore-pipfile

python manage.py collectstatic --no-input

python manage.py makemigrations 

python manage.py migrate