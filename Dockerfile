FROM mysql:8.0


COPY ./db_tabela/ /docker-entrypoint-initdb.d/