from app.models import Professor, db

def create_professor(nome, especialidade):
    professor = Professor(nome=nome, especialidade=especialidade)
    db.session.add(professor)
    db.session.commit()

def get_professor_by_id(id):
    return Professor.query.get(id)

def get_all_professores():
    return Professor.query.all()

def update_professor(id, nome, especialidade):
    professor = Professor.query.get(id)
    if professor:
        professor.nome = nome
        professor.especialidade = especialidade
        db.session.commit()

def delete_professor(id):
    professor = Professor.query.get(id)
    if professor:
        db.session.delete(professor)
        db.session.commit()
