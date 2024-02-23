#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip && pip install pipenv

pipenv lock

pip install pipenv && pipenv install --system --deploy

python manage.py collectstatic --no-input

python manage.py migrate