# Usar imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos do projeto para dentro do contêiner
COPY . /app

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Definir a variável de ambiente para Flask
ENV FLASK_APP=app
ENV FLASK_ENV=development

# Expõe a porta 5000, que é a padrão para o Flask
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
