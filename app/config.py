import os

class Config:
    # URL do banco de dados PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://usuario:senha@localhost:5432/nome_do_banco')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desabilita a notificação de alterações de objetos
