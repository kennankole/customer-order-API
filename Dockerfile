FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    python3-dev \
    libpq-dev \
    postgresql-client \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pipenv lock

RUN pip install pipenv && pipenv install --system --deploy

COPY . /app/

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "backendAPI.wsgi:application"]
