from flask import Blueprint, request, jsonify
from app.crud.crudAtividade import create_atividade, get_atividade_by_id, get_all_atividades, update_atividade, delete_atividade
from app.crud.crudPagamento import create_pagamento, get_pagamento_by_id, get_all_pagamentos, update_pagamento, delete_pagamento
from app.crud.crudPresenca import create_presenca, get_presenca_by_id, get_all_presencas, update_presenca, delete_presenca
from app.crud.crudProfessor import create_professor, get_professor_by_id, get_all_professores, update_professor, delete_professor
from app.crud.crudTurma import create_turma, get_turma_by_id, get_all_turmas, update_turma, delete_turma
from app.crud.crudUsuario import create_usuario, get_usuario_by_id, get_all_usuarios, update_usuario, delete_usuario

main_routes = Blueprint('main_routes', __name__)

# ---------- Atividades ----------
@main_routes.route('/atividade', methods=['POST'])
def add_atividade():
    data = request.get_json()
    create_atividade(data['nome'], data.get('descricao'))
    return jsonify({"message": "Atividade criada com sucesso!"}), 201

@main_routes.route('/atividade/<int:id>', methods=['GET'])
def get_atividade(id):
    atividade = get_atividade_by_id(id)
    if atividade:
        return jsonify({"id": atividade.id, "nome": atividade.nome, "descricao": atividade.descricao})
    return jsonify({"message": "Atividade não encontrada!"}), 404

@main_routes.route('/atividades', methods=['GET'])
def listar_atividades():
    atividades = get_all_atividades()
    return jsonify([{"id": a.id, "nome": a.nome, "descricao": a.descricao} for a in atividades])

@main_routes.route('/atividade/<int:id>', methods=['PUT'])
def atualizar_atividade(id):
    data = request.get_json()
    update_atividade(id, data['nome'], data.get('descricao'))
    return jsonify({"message": "Atividade atualizada com sucesso!"})

@main_routes.route('/atividade/<int:id>', methods=['DELETE'])
def remover_atividade(id):
    delete_atividade(id)
    return jsonify({"message": "Atividade removida com sucesso!"})

# ---------- Pagamentos ----------
@main_routes.route('/pagamento', methods=['POST'])
def add_pagamento():
    data = request.get_json()
    create_pagamento(data['aluno_id'], data['valor'], data['data'])
    return jsonify({"message": "Pagamento registrado com sucesso!"}), 201

@main_routes.route('/pagamento/<int:id>', methods=['GET'])
def get_pagamento(id):
    pagamento = get_pagamento_by_id(id)
    if pagamento:
        return jsonify({"id": pagamento.id, "aluno_id": pagamento.aluno_id, "valor": pagamento.valor, "data": pagamento.data})
    return jsonify({"message": "Pagamento não encontrado!"}), 404

@main_routes.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    pagamentos = get_all_pagamentos()
    return jsonify([{"id": p.id, "aluno_id": p.aluno_id, "valor": p.valor, "data": p.data} for p in pagamentos])

@main_routes.route('/pagamento/<int:id>', methods=['PUT'])
def atualizar_pagamento(id):
    data = request.get_json()
    update_pagamento(id, data['aluno_id'], data['valor'], data['data'])
    return jsonify({"message": "Pagamento atualizado com sucesso!"})

@main_routes.route('/pagamento/<int:id>', methods=['DELETE'])
def remover_pagamento(id):
    delete_pagamento(id)
    return jsonify({"message": "Pagamento removido com sucesso!"})

# ---------- Presenças ----------
@main_routes.route('/presenca', methods=['POST'])
def add_presenca():
    data = request.get_json()
    create_presenca(data['aluno_id'], data['data'], data['presente'])
    return jsonify({"message": "Presença registrada com sucesso!"}), 201

@main_routes.route('/presenca/<int:id>', methods=['GET'])
def get_presenca(id):
    presenca = get_presenca_by_id(id)
    if presenca:
        return jsonify({"id": presenca.id, "aluno_id": presenca.aluno_id, "data": presenca.data, "presente": presenca.presente})
    return jsonify({"message": "Presença não encontrada!"}), 404

@main_routes.route('/presencas', methods=['GET'])
def listar_presencas():
    presencas = get_all_presencas()
    return jsonify([{"id": p.id, "aluno_id": p.aluno_id, "data": p.data, "presente": p.presente} for p in presencas])

@main_routes.route('/presenca/<int:id>', methods=['PUT'])
def atualizar_presenca(id):
    data = request.get_json()
    update_presenca(id, data['aluno_id'], data['data'], data['presente'])
    return jsonify({"message": "Presença atualizada com sucesso!"})

@main_routes.route('/presenca/<int:id>', methods=['DELETE'])
def remover_presenca(id):
    delete_presenca(id)
    return jsonify({"message": "Presença removida com sucesso!"})

# ---------- Professores ----------
@main_routes.route('/professor', methods=['POST'])
def add_professor():
    data = request.get_json()
    create_professor(data['nome'], data['formacao'])
    return jsonify({"message": "Professor criado com sucesso!"}), 201

@main_routes.route('/professor/<int:id>', methods=['GET'])
def get_professor(id):
    professor = get_professor_by_id(id)
    if professor:
        return jsonify({"id": professor.id, "nome": professor.nome, "formacao": professor.formacao})
    return jsonify({"message": "Professor não encontrado!"}), 404

@main_routes.route('/professores', methods=['GET'])
def listar_professores():
    professores = get_all_professores()
    return jsonify([{"id": p.id, "nome": p.nome, "formacao": p.formacao} for p in professores])

@main_routes.route('/professor/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    data = request.get_json()
    update_professor(id, data['nome'], data['formacao'])
    return jsonify({"message": "Professor atualizado com sucesso!"})

@main_routes.route('/professor/<int:id>', methods=['DELETE'])
def remover_professor(id):
    delete_professor(id)
    return jsonify({"message": "Professor removido com sucesso!"})

# ---------- Turmas ----------
@main_routes.route('/turma', methods=['POST'])
def add_turma():
    data = request.get_json()
    create_turma(data['nome'], data['periodo'])
    return jsonify({"message": "Turma criada com sucesso!"}), 201

@main_routes.route('/turma/<int:id>', methods=['GET'])
def get_turma(id):
    turma = get_turma_by_id(id)
    if turma:
        return jsonify({"id": turma.id, "nome": turma.nome, "periodo": turma.periodo})
    return jsonify({"message": "Turma não encontrada!"}), 404

@main_routes.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = get_all_turmas()
    return jsonify([{"id": t.id, "nome": t.nome, "periodo": t.periodo} for t in turmas])

@main_routes.route('/turma/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    data = request.get_json()
    update_turma(id, data['nome'], data['periodo'])
    return jsonify({"message": "Turma atualizada com sucesso!"})

@main_routes.route('/turma/<int:id>', methods=['DELETE'])
def remover_turma(id):
    delete_turma(id)
    return jsonify({"message": "Turma removida com sucesso!"})

# ---------- Usuários ----------
@main_routes.route('/usuario', methods=['POST'])
def add_usuario():
    data = request.get_json()
    create_usuario(data['username'], data['password'], data['role'])
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@main_routes.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = get_usuario_by_id(id)
    if usuario:
        return jsonify({"id": usuario.id, "username": usuario.username, "role": usuario.role})
    return jsonify({"message": "Usuário não encontrado!"}), 404

@main_routes.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = get_all_usuarios()
    return jsonify([{"id": u.id, "username": u.username, "role": u.role} for u in usuarios])

@main_routes.route('/usuario/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.get_json()
    update_usuario(id, data['username'], data['password'], data['role'])
    return jsonify({"message": "Usuário atualizado com sucesso!"})

@main_routes.route('/usuario/<int:id>', methods=['DELETE'])
def remover_usuario(id):
    delete_usuario(id)
    return jsonify({"message": "Usuário removido com sucesso!"})
