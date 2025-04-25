from flask_sqlalchemy import SQLAlchemy

# Instanciando o objeto db
db = SQLAlchemy()

# Tabela User (Usuários)
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Tabela Course (Cursos)
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f'<Course {self.name}>'

# Tabela Enrollment (Matrículas)
class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    date_enrolled = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')

    def __repr__(self):
        return f'<Enrollment User {self.user_id} - Course {self.course_id}>'

# Relacionamentos
User.enrollments = db.relationship('Enrollment', back_populates='user', cascade='all, delete-orphan')
Course.enrollments = db.relationship('Enrollment', back_populates='course', cascade='all, delete-orphan')
from . import db

class Atividade(db.Model):
    __tablename__ = 'atividade'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Pagamento(db.Model):
    __tablename__ = 'pagamento'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)

    def __init__(self, aluno_id, valor, data):
        self.aluno_id = aluno_id
        self.valor = valor
        self.data = data

class Presenca(db.Model):
    __tablename__ = 'presenca'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    presente = db.Column(db.Boolean, nullable=False)

    def __init__(self, aluno_id, data, presente):
        self.aluno_id = aluno_id
        self.data = data
        self.presente = presente

class Professor(db.Model):
    __tablename__ = 'professor'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
