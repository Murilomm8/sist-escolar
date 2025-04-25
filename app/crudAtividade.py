from app.models import Atividade, db

def create_atividade(nome, descricao):
    atividade = Atividade(nome=nome, descricao=descricao)
    db.session.add(atividade)
    db.session.commit()

def get_atividade_by_id(id):
    return Atividade.query.get(id)

def get_all_atividades():
    return Atividade.query.all()

def update_atividade(id, nome, descricao):
    atividade = Atividade.query.get(id)
    if atividade:
        atividade.nome = nome
        atividade.descricao = descricao
        db.session.commit()

def delete_atividade(id):
    atividade = Atividade.query.get(id)
    if atividade:
        db.session.delete(atividade)
        db.session.commit()
