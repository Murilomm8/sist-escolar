from app.models import Presenca, db

def create_presenca(aluno_id, data, presente):
    presenca = Presenca(aluno_id=aluno_id, data=data, presente=presente)
    db.session.add(presenca)
    db.session.commit()

def get_presenca_by_id(id):
    return Presenca.query.get(id)

def get_all_presencas():
    return Presenca.query.all()

def update_presenca(id, aluno_id, data, presente):
    presenca = Presenca.query.get(id)
    if presenca:
        presenca.aluno_id = aluno_id
        presenca.data = data
        presenca.presente = presente
        db.session.commit()

def delete_presenca(id):
    presenca = Presenca.query.get(id)
    if presenca:
        db.session.delete(presenca)
        db.session.commit()
