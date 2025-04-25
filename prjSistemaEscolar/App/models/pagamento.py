# app/models/pagamento.py

from app.models import db
from datetime import datetime

class Pagamento(db.Model):
    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)
    data_pagamento = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)

    aluno = db.relationship('Aluno', backref='pagamentos')

    def __repr__(self):
        return f'<Pagamento {self.id} - {self.valor}>'
