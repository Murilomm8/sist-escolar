# app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# app/models/__init__.py

from .aluno import Aluno
from .atividade import Atividade
from .presenca import Presenca
from .professor import Professor
from .pagamento import Pagamento
from .turma import Turma
from .usuario import Usuario  # Adiciona a importação do modelo Usuario
from app import db
