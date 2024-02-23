#!/usr/bin/env bash
set -o errexit

pipenv install --ignore-pipfile

pipenv install typing_extensions

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate