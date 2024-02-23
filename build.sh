#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip && pip install pipenv

pipenv lock

pipenv install

python manage.py collectstatic --no-input

python manage.py migrate