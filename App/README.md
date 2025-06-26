# Sis-esco API – Back-end de Gestão Escolar

Back-end RESTful para um sistema de gestão escolar, desenvolvido em Python com Flask, SQLAlchemy e Flasgger (Swagger UI).  
Dados persistidos em SQLite (`school.db`). Contêinerizado com Docker.

---

##  Arquitetura

- **Framework**: Flask  
- **ORM**: SQLAlchemy  
- **Documentação**: Flasgger (OpenAPI/Swagger UI)  
- **Banco de Dados**: SQLite (arquivo `school.db`)  
- **Docker**: python:3.9-slim  

---

##  Recursos implementados

| Recurso               | Rota Base                | Métodos       |
| --------------------- | ------------------------ | ------------- |
| **Pagamentos**        | `/payments`              | GET, POST, PUT, DELETE |
| **Presenças**         | `/attendances`           | GET, POST, PUT, DELETE |
| **Atividades**        | `/activities`            | GET, POST, PUT, DELETE |
| **Alunos**            | `/students`              | GET, POST, PUT, DELETE |
| **Professores**       | `/professors`            | GET, POST, PUT, DELETE |
| **Disciplinas**       | `/disciplines`           | GET, POST, PUT, DELETE |
| **Turmas**            | `/classes`               | GET, POST, PUT, DELETE |
| **Matrículas**        | `/enrollments`           | GET, POST, DELETE       |
| **Notas**             | `/grades`                | GET, POST, PUT, DELETE |
| **Frequência Acadêmica** | `/academic_attendance` | GET, POST, PUT, DELETE |
| **DB Init**           | `/initdb`                | GET (recria todas as tabelas) |

---

##  Requisitos

- **Sem Docker**  
  - Python 3.9+  
  - pip  

- **Com Docker**  
  - Docker Engine 20.10+  

---

##  Instalação e Execução

### 1) Sem Docker

```bash
# 1. Clone e entre na pasta APP
git clone https://github.com/Murilomm8/sist-escolar.git
cd sist-escolar/APP

# 2. (Opcional) Virtualenv
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# 3. Instale dependências
pip install --upgrade pip
pip install -r requirements.txt

# 4. Inicialize o banco (apaga e recria tabelas)
curl -X GET http://localhost:5000/initdb

# 5. Inicie a aplicação
python app.py
A API ficará disponível em http://localhost:5000/.

2) Com Docker
bash
# 1. Na raiz do projeto (onde está o Dockerfile)
docker build -t sis-esco-api .

# 2. Crie e rode o container
docker run -d \
  --name sis-esco \
  -p 5000:5000 \
  -v $(pwd)/APP/school.db:/app/school.db \
  sis-esco-api

# 3. Verifique
docker ps
docker logs sis-esco

# 4. Pare / Remova
docker stop sis-esco
docker rm sis-esco
 Documentação Swagger (OpenAPI)
Abra no navegador:

http://localhost:5000/api/docs
 Exemplos de uso (cURL)
> Substitua localhost:5000 conforme seu ambiente.

Pagamentos
bash
# Listar
curl -X GET http://localhost:5000/payments

# Criar
curl -X POST http://localhost:5000/payments \
  -H "Content-Type: application/json" \
  -d '{"student_name":"João Silva","amount":150.00}'

# Atualizar
curl -X PUT http://localhost:5000/payments/1 \
  -H "Content-Type: application/json" \
  -d '{"status":"pago"}'

# Deletar
curl -X DELETE http://localhost:5000/payments/1
Presenças
bash
curl -X GET "http://localhost:5000/attendances?student_name=Maria"

curl -X POST http://localhost:5000/attendances \
  -H "Content-Type: application/json" \
  -d '{"student_name":"Maria","date":"2025-06-20","present":true}'
Atividades
bash
curl -X GET http://localhost:5000/activities

curl -X POST http://localhost:5000/activities \
  -H "Content-Type: application/json" \
  -d '{"student_name":"Lucas","description":"Dever de casa - Matemática"}'
Alunos
bash
curl -X GET http://localhost:5000/students

curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Paula","birth_date":"2020-01-15"}'

curl -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana P.","birth_date":"2020-01-16"}'

curl -X DELETE http://localhost:5000/students/1
Professores
bash
curl -X GET http://localhost:5000/professors

curl -X POST http://localhost:5000/professors \
  -H "Content-Type: application/json" \
  -d '{"name":"Carlos Lima","specialty":"Pedagogia","contact":"(11)99999-0000","registry":"PRF-1234"}'
Disciplinas
bash
curl -X GET http://localhost:5000/disciplines

curl -X POST http://localhost:5000/disciplines \
  -H "Content-Type: application/json" \
  -d '{"name":"Matemática","code":"MAT101","workload":60}'
Turmas
bash
curl -X GET http://localhost:5000/classes

curl -X POST http://localhost:5000/classes \
  -H "Content-Type: application/json" \
  -d '{"identifier":"A1","year":2025}'
Matrículas
bash
# Listar
curl -X GET http://localhost:5000/enrollments

# Matricular
curl -X POST http://localhost:5000/enrollments \
  -H "Content-Type: application/json" \
  -d '{"student_id":1,"class_id":2}'

# Desmatricular
curl -X DELETE "http://localhost:5000/enrollments?student_id=1&class_id=2"
Notas
bash
curl -X GET http://localhost:5000/grades

curl -X POST http://localhost:5000/grades \
  -H "Content-Type: application/json" \
  -d '{"student_id":1,"discipline_id":3,"grade":8.5}'
Frequência Acadêmica
bash
curl -X GET http://localhost:5000/academic_attendance

curl -X POST http://localhost:5000/academic_attendance \
  -H "Content-Type: application/json" \
  -d '{"student_id":1,"discipline_id":3,"presences":12}'
Banco de Dados
bash
curl -X GET http://localhost:5000/initdb
 Estrutura de arquivos
sist-escolar/
├── APP/
├── Dockerfile
├── README.md
├── app.py
├── models.py
├── pip
├── requirements.txt
├── routes.py
└── school.db
 Próximos passos
Ajustar validações e mensagens de erro.

Migrar para PostgreSQL/MySQL em produção.

Implementar autenticação (JWT).

Criar testes automatizados (pytest).
