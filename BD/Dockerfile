# Placeholder: Este Dockerfile pode ser adaptado para criar um container para o SGBD desejado.
# Exemplo com SQLite (para desenvolvimento) não é o ideal para produção.
# Para uso em produção, recomenda-se utilizar PostgreSQL ou MySQL com as respectivas configurações.

FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y sqlite3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /data

CMD ["sqlite3", "school.db"]
