from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/v1/alunos', methods=['GET'])
def listar_alunos():
    """
    Recupera a lista de alunos.
    ---
    responses:
      200:
        description: Lista de alunos.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              nome:
                type: string
                example: "João Silva"
              idade:
                type: integer
                example: 5
    """
    alunos = [
        {"id": 1, "nome": "João Silva", "idade": 5},
        {"id": 2, "nome": "Maria Oliveira", "idade": 4}
    ]
    return jsonify({"alunos": alunos})

if __name__ == "__main__":
    app.run(debug=True)
