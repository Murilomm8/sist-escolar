# Usa a imagem oficial do PostgreSQL
FROM postgres:14-alpine

# Variáveis de ambiente
ENV POSTGRES_DB=escola
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=123456

# Copia e executa o DDL na inicialização do container
COPY arquivo.sql /docker-entrypoint-initdb.d/

# Expõe a porta padrão do Postgres
EXPOSE 5432
