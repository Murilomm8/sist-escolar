from app import db

class Turma(db.Model):
    __tablename__ = 'turma'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

    def __repr__(self):
        return f"<Turma {self.nome} - {self.periodo}>"
