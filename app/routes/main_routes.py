from flask import Blueprint, request, jsonify
from app.crud.crudAtividade import create_atividade, get_atividade_by_id, get_all_atividades, update_atividade, delete_atividade
from app.crud.crudPagamento import create_pagamento, get_pagamento_by_id, get_all_pagamentos, update_pagamento, delete_pagamento
from app.crud.crudPresenca import create_presenca, get_presenca_by_id, get_all_presencas, update_presenca, delete_presenca
from app.crud.crudProfessor import create_professor, get_professor_by_id, get_all_professores, update_professor, delete_professor
from app.crud.crudTurma import create_turma, get_turma_by_id, get_all_turmas, update_turma, delete_turma
from app.crud.crudUsuario import create_usuario, get_usuario_by_id, get_all_usuarios, update_usuario, delete_usuario

main_routes = Blueprint('main_routes', __name__)

# Atividade Routes
@main_routes.route('/atividade', methods=['POST'])
def add_atividade():
    data = request.get_json()
    create_atividade(data['nome'], data.get('descricao'))
    return jsonify({"message": "Atividade criada com sucesso!"})

@main_routes.route('/atividade/<int:id>', methods=['GET'])
def get_atividade(id):
    atividade = get_atividade_by_id(id)
    if atividade:
        return jsonify({"id": atividade.id, "nome": atividade.nome, "descricao": atividade.descricao})
    return jsonify({"message": "Atividade não encontrada!"}), 404

# Repetir as rotas para os outros modelos (Pagamento, Presença, Professor, Turma, Usuario)
# Exemplos de rotas para Pagamento:
@main_routes.route('/pagamento', methods=['POST'])
def add_pagamento():
    data = request.get_json()
    create_pagamento(data['aluno_id'], data['valor'], data['data'])
    return jsonify({"message": "Pagamento registrado com sucesso!"})

@main_routes.route('/pagamento/<int:id>', methods=['GET'])
def get_pagamento(id):
    pagamento = get_pagamento_by_id(id)
    if pagamento:
        return jsonify({"id": pagamento.id, "aluno_id": pagamento.aluno_id, "valor": pagamento.valor, "data": pagamento.data})
    return jsonify({"message": "Pagamento não encontrado!"}), 404

# Continue com as rotas para Presença, Professor, Turma, e Usuario.
