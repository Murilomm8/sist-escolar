🚀 Sis-Esco - Sistema de Gestão Escolar
Sis-Esco é uma API REST desenvolvida em Python com o framework Flask, utilizando Flask_SQLAlchemy para persistência de dados e Flasgger para a documentação de endpoints com Swagger.

A API permite o gerenciamento de pagamentos, presenças e atividades escolares, tornando o fluxo administrativo mais eficiente.

-----------------------------------------------------------------------
🛠 Tecnologias Utilizadas

Python 3.9+

Flask (Framework Web)

Flask_SQLAlchemy (Banco de Dados com ORM)

Flasgger (Swagger UI para documentação)

Docker (Conteinerização para facilitar a execução)

SQLite (Banco de Dados leve para desenvolvimento)

Prometheus & Grafana (Monitoramento da aplicação)

-----------------------------------------------------------------------

Estrutura do código

sis-esco/

├── App/                   # Código-fonte da API

│   ├── app.py             # Código principal (Flask API)

│   ├── requirements.txt   # Lista de dependências do Python

│   ├── Dockerfile         # Dockerfile para rodar a API

│   └── README.md          # Instruções da aplicação

├── BD/                    # Configuração do Banco de Dados

│   ├── arquivo.sql        # Script DDL para criação do BD

│   ├── Dockerfile         # Dockerfile do banco de dados (se necessário)

│   └── README.md          # Instruções para o BD

└── Observabilidade/        # Monitoramento

    ├── prometheus/        # Configuração do Prometheus
		
    ├── grafana/           # Configuração do Grafana  
		
-----------------------------------------------------------------------

🚀 Como Rodar a Aplicação

✅ Rodando a API com Docker

1.Certifique-se de que o Docker está instalado e rodando no sistema.

2.Navegue até a pasta App/ e execute o comando para construir a imagem:

docker build -t sis-esco .

3.Agora, inicie o container:

docker run -d -p 5000:5000 sis-esco

4.Acesse no navegador:

http://localhost:5000/

-----------------------------------------------------------------------

✅ Rodando a API sem Docker

Caso prefira rodar sem Docker, siga os seguintes passos:

1.Crie um ambiente virtual (recomendado para evitar conflitos de dependências):

python -m venv venv

2.Ative o ambiente virtual:

Windows (PowerShell):

.\venv\Scripts\Activate.ps1

3.Instale as dependências:

pip install -r requirements.txt

4.Inicie a aplicação Flask:

python app.py

5.Acesse a API no navegador:

http://localhost:5000/

-----------------------------------------------------------------------

📖 Acessando a Documentação Swagger

Todos os endpoints CRUD da API estão documentados no Swagger UI.

1.Inicie a API (com Docker ou sem Docker).

2.Abra o navegador e acesse:

http://localhost:5000/api/docs

-----------------------------------------------------------------------

🔄 Endpoints CRUD Disponíveis

📌 Pagamentos (/payments)

GET /payments → Listar todos os pagamentos.

POST /payments → Criar um novo pagamento { "student_name": "João", "amount": 150.0 }.

📌 Presenças (/attendances)

GET /attendances → Listar todas as presenças (aceita filtro ?student_name=João).

POST /attendances → Registrar presença { "student_name": "Maria", "date": "2025-04-27", "present": true }.

📌 Atividades (/activities)

GET /activities → Listar todas as atividades.

POST /activities → Registrar uma nova atividade { "student_name": "Lucas", "description": "Desenho feito em aula" }.

📌 Reinicializar Banco (/initdb)

GET /initdb → Apaga e recria o banco de dados (⚠️ Apenas em ambiente de desenvolvimento).

-----------------------------------------------------------------------
🤝 Contribuições

Quer contribuir com o projeto? Siga os passos:

1.Clone o repositório:

git clone https://github.com/seu-usuario/sis-esco.git

2.Crie uma branch para suas alterações:

git checkout -b feature-minha-melhoria

3.Faça as modificações e envie para análise:

git add .

git commit -m "Adicionando melhoria na API"

git push origin feature-minha-melhoria

4.Abra um Pull Request no GitHub 🎉

-----------------------------------------------------------------------
