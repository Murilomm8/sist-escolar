# Utiliza uma imagem oficial do Python (versão 3.9) como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt ./

# Instala as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação para o container
COPY . .

# Expõe a porta 5000 onde a API estará disponível
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
