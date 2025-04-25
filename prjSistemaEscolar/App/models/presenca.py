# app/models/presenca.py

from app.models import db
from datetime import datetime

class Presenca(db.Model):
    __tablename__ = 'presencas'

    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunos.id'), nullable=False)
    data_presenca = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False)  # Pode ser 'Presente', 'Ausente', etc.
    
    aluno = db.relationship('Aluno', backref='presencas', lazy=True)

    def __repr__(self):
        return f'<Presenca {self.id} - Aluno {self.aluno_id} - Status {self.status}>'
