from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Criação da instância do app
app = Flask(__name__)
app.config.from_object(Config)

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Importa os models e os cruds
from app import models
from app.crud import crudAtividade, crudPagamento, crudPresenca, crudProfessor, crudTurma, crudUsuario

# Aqui você pode adicionar as rotas, etc.
