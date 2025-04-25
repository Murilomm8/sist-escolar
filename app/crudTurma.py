from app.models import Turma, db

def create_turma(nome, periodo):
    turma = Turma(nome=nome, periodo=periodo)
    db.session.add(turma)
    db.session.commit()

def get_turma_by_id(id):
    return Turma.query.get(id)

def get_all_turmas():
    return Turma.query.all()

def update_turma(id, nome, periodo):
    turma = Turma.query.get(id)
    if turma:
        turma.nome = nome
        turma.periodo = periodo
        db.session.commit()

def delete_turma(id):
    turma = Turma.query.get(id)
    if turma:
        db.session.delete(turma)
        db.session.commit()
