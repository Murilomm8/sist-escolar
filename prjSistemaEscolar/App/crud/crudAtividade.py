from app.models import Atividade, db
from sqlalchemy.exc import SQLAlchemyError

def create_atividade(nome, descricao):
    try:
        # Criação de uma nova atividade
        atividade = Atividade(nome=nome, descricao=descricao)
        db.session.add(atividade)
        db.session.commit()
        return atividade
    except SQLAlchemyError as e:
        db.session.rollback()  # Em caso de erro, reverte a transação
        return str(e)  # Retorna a mensagem de erro

def get_atividade_by_id(id):
    try:
        # Busca uma atividade pelo ID
        return Atividade.query.get(id)
    except SQLAlchemyError as e:
        return str(e)  # Em caso de erro, retorna a mensagem

def get_all_atividades():
    try:
        # Retorna todas as atividades
        return Atividade.query.all()
    except SQLAlchemyError as e:
        return str(e)  # Em caso de erro, retorna a mensagem

def update_atividade(id, nome, descricao):
    try:
        # Atualiza uma atividade existente
        atividade = Atividade.query.get(id)
        if atividade:
            atividade.nome = nome
            atividade.descricao = descricao
            db.session.commit()
            return atividade
        else:
            return "Atividade não encontrada."
    except SQLAlchemyError as e:
        db.session.rollback()  # Reverte a transação em caso de erro
        return str(e)  # Retorna a mensagem de erro

def delete_atividade(id):
    try:
        # Deleta uma atividade pelo ID
        atividade = Atividade.query.get(id)
        if atividade:
            db.session.delete(atividade)
            db.session.commit()
            return "Atividade deletada com sucesso."
        else:
            return "Atividade não encontrada."
    except SQLAlchemyError as e:
        db.session.rollback()  # Reverte a transação em caso de erro
        return str(e)  # Retorna a mensagem de erro
