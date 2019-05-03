FROM postgres:alpine

COPY ./postgresql.conf /var/lib/postgresql
COPY ./createdb.sql /var/lib/postgresql

EXPOSE 5432

CMD ["postgres", "-D", "/var/lib/postgresql/data", "-c", "config_file=/var/lib/postgresql/postgresql.conf"]
