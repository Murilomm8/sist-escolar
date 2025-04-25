from app.models import Pagamento, db

def create_pagamento(aluno_id, valor, data):
    pagamento = Pagamento(aluno_id=aluno_id, valor=valor, data=data)
    db.session.add(pagamento)
    db.session.commit()

def get_pagamento_by_id(id):
    return Pagamento.query.get(id)

def get_all_pagamentos():
    return Pagamento.query.all()

def update_pagamento(id, aluno_id, valor, data):
    pagamento = Pagamento.query.get(id)
    if pagamento:
        pagamento.aluno_id = aluno_id
        pagamento.valor = valor
        pagamento.data = data
        db.session.commit()

def delete_pagamento(id):
    pagamento = Pagamento.query.get(id)
    if pagamento:
        db.session.delete(pagamento)
        db.session.commit()
