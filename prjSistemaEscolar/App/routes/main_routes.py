from flask import Blueprint, jsonify
from flasgger import swag_from
from app.models.aluno import Aluno

main_routes = Blueprint('main', __name__)

@main_routes.route('/api/alunos', methods=['GET'])
@swag_from({
    'tags': ['Alunos'],
    'description': 'Obtém todos os alunos.',
    'responses': {
        '200': {
            'description': 'Lista de alunos.',
            'examples': {
                'application/json': [
                    {"id": 1, "nome": "João", "idade": 8},
                    {"id": 2, "nome": "Maria", "idade": 7}
                ]
            }
        }
    }
})
def get_alunos():
    alunos = [{"id": 1, "nome": "João", "idade": 8}, {"id": 2, "nome": "Maria", "idade": 7}]
    return jsonify(alunos)
