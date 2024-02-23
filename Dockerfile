FROM python:3.9

ENV HOME=/home/
ENV APP_HOME=/home/app/
RUN mkdir ${APP_HOME}
RUN mkdir ${APP_HOME}/staticfiles
WORKDIR ${APP_HOME}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    python3-dev \
    libpq-dev \
    postgresql-client \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install pipenv


COPY Pipfile Pipfile.lock ./

RUN pipenv lock

RUN pip install pipenv && pipenv install --system --deploy

COPY . .

EXPOSE 8000

