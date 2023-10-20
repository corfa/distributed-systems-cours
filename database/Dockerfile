
FROM postgres


COPY .env /app/.env


RUN set -a && . /app/.env && set +a


ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}


COPY init.sql /docker-entrypoint-initdb.d/

