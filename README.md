# 🚀 Sis-Esco - Sistema de Gestão Escolar

**Sis-Esco** é uma API REST desenvolvida em **Python** com o framework **Flask**, utilizando **Flask_SQLAlchemy** para persistência de dados, **Flasgger** para documentar os endpoints via Swagger e, para o monitoramento, as ferramentas **Prometheus** e **Grafana**. O sistema facilita o gerenciamento de pagamentos, presenças, atividades e cadastros de alunos, otimizando o fluxo administrativo do ambiente escolar.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.9+**
- **Flask** (Framework Web)
- **Flask_SQLAlchemy** (ORM para manipulação do Banco de Dados)
- **Flasgger** (Interface Swagger para documentação dos endpoints)
- **Docker & Docker Compose** (Conteinerização e orquestração)
- **SQLite** (Banco de Dados leve para desenvolvimento – API)
- **PostgreSQL** (Utilizado com observabilidade, se necessário)
- **Prometheus & Grafana** (Monitoramento do Sistema e do Banco de Dados)

---

## 📐 Estrutura do Projeto


sis-esco/

├── App/# Código-fonte da API

│   ├── app.py# Código principal (Flask API)

│   ├── requirements.txt# Lista de dependências do Python

│   ├── Dockerfile# Dockerfile para rodar a API

│   └── README.md# Instruções da aplicação

├── BD/# Configuração do Banco de Dados

│   ├── arquivo.sql# Script DDL para criação do BD

│   ├── Dockerfil# Dockerfile do banco de dados (se necessário)

│   └── README.md# Instruções para o BD

└── Observabilidade/# Monitoramento

    ├── prometheus/# Configuração do Prometheus
		
    ├── grafana/ # Configuração do Grafana  
├──Readme.md

├──docker-compose.yml

---

## 🚀 Como Rodar a Aplicação

### ✅ Rodando a API com Docker

1. **Pré-requisitos:**  
   - Certifique-se de que o Docker (e o Docker Compose) estejam instalados e executando.

2. **Navegue até a pasta raiz do projeto:**
   ```bash
   cd sis-esco

3. Inicialize o ambiente completo (App + Observabilidade) com Docker Compose:
docker-compose up -d

###> O que acontece: > - Um container para o PostgreSQL (banco de dados) será provisionado. > - O postgres_exporter será iniciado para coletar métricas do PostgreSQL. > - O Prometheus iniciará e fará scrape das métricas do postgres_exporter. > - O Grafana ficará disponível para a criação e visualização de dashboards. > - A API (se provisionada via Dockerfile da pasta App) estará rodando na porta 5000.

4. Verifique se os containers estão ativos:
docker ps

5. Acessando a API:
API: http://localhost:5000/
Documentação Swagger (endpoints CRUD): http://localhost:5000/api/docs

---

✅ Rodando a API sem Docker

1. Crie um ambiente virtual (recomendado):
python -m venv venv

2. Ative o ambiente virtual:
Windows (PowerShell):
.\venv\Scripts\Activate.ps1

3. Instale as dependências:
pip install -r App/requirements.txt

4. Inicie a aplicação Flask:
python App/app.py

5. Acesse a API:
Navegador: http://localhost:5000/
Documentação Swagger: http://localhost:5000/api/docs

---

📖 Acessando a Documentação Swagger

Todos os endpoints CRUD da API estão documentados no Swagger UI.

1. Inicie a API (com Docker ou sem Docker).

2. Abra o navegador e acesse:
http://localhost:5000/api/docs

---

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

---

📊 Monitoramento (Observabilidade do BD)
O ambiente de observabilidade é configurado via Docker Compose e integra:

PostgreSQL: Servidor de BD utilizado pelo sistema.

postgres_exporter: Exporta métricas do PostgreSQL.

Prometheus: Coleta as métricas do exportador.

Grafana: Permite criar dashboards interativos para visualizar essas métricas.

Para acessar:
Prometheus: http://localhost:9090
test: flask_http_request_total

Grafana: http://localhost:3000 (Login padrão: admin/admin – configure o Prometheus como Data Source com URL http://prometheus-sis-esco:9090 ou http://localhost:9090)

Com o Grafana, você poderá visualizar métricas como:

Número de conexões ativas.

Taxa de transações/consultas.

Utilização de recursos (CPU, memória, disco) do PostgreSQL.

Tamanho e crescimento do BD.

Métricas de locks e contendas, entre outras.

(teste com grafane em /script/test.json)
---

🚀 Observabilidade com Docker Compose
O arquivo docker-compose.yml na raiz do projeto provisiona os seguintes serviços:

PostgreSQL: Container para o banco de dados.

postgres_exporter: Para exportar métricas do PostgreSQL.

Prometheus: Para coletar e armazenar as métricas.

Grafana: Para visualização e criação de dashboards.

---

🤝 Contribuições

Quer contribuir com o projeto? Siga os passos:

1. Clone o repositório:

git clone https://github.com/Murilomm8/sist-escolar.git

2. Crie uma branch para suas alterações:

git checkout -b feature-minha-melhoria

3. Faça as modificações e envie para análise:

git add .

git commit -m "Adicionando melhoria na API"

git push origin feature-minha-melhoria

4. Abra um Pull Request no GitHub 🎉

---
