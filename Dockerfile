FROM python:3.9

RUN mkdir - /home/app

RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
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

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]

