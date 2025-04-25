# app/models/atividade.py

from app.models import db
from datetime import datetime

class Atividade(db.Model):
    __tablename__ = 'atividades'

    # Definindo as colunas da tabela 'atividades'
    id = db.Column(db.Integer, primary_key=True)  # Identificador único da atividade
    nome = db.Column(db.String(100), nullable=False)  # Nome da atividade (não pode ser nulo)
    descricao = db.Column(db.Text, nullable=True)  # Descrição da atividade (pode ser nula)
    data_entrega = db.Column(db.DateTime, nullable=True)  # Data de entrega (pode ser nula)
    concluida = db.Column(db.Boolean, default=False)  # Status da atividade (default: não concluída)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)  # Data e hora de criação (default: atual)

    # Representação em string do modelo, para facilitar a leitura dos objetos em logs ou prints
    def __repr__(self):
        return f'<Atividade {self.id} - {self.nome}>'

    # Método para marcar a atividade como concluída
    def concluir(self):
        self.concluida = True
        db.session.commit()

    # Método para atualizar a descrição da atividade
    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao
        db.session.commit()

    # Método para verificar se a atividade está atrasada com base na data de entrega
    def esta_atrasada(self):
        if self.data_entrega and self.data_entrega < datetime.utcnow() and not self.concluida:
            return True
        return False
