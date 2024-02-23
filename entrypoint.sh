#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
  echo "Waiting for postgres..."
  while ! nc -z $HOST $PORT; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

exec "$@"