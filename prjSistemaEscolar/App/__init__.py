from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
# Cria a instância do Swagger
api = Api(app, version='1.0', title='Sistema Escolar API',
          description='Uma API para gerenciar o sistema escolar.',
          doc='/api/docs')  # URL para acessar a documentação

# Definindo o modelo de dados com Swagger
student_model = api.model('Student', {
    'id': fields.Integer(required=True, description='ID do estudante'),
    'name': fields.String(required=True, description='Nome do estudante'),
    'age': fields.Integer(required=True, description='Idade do estudante')
})

# Endpoints (CRU - Create, Read, Update)
students = []

@api.route('/students')
class StudentList(Resource):
    @api.doc(description="Retorna todos os estudantes")
    def get(self):
        return students, 200

    @api.doc(description="Adiciona um novo estudante")
    @api.expect(student_model)
    def post(self):
        student = api.payload
        students.append(student)
        return student, 201

@api.route('/students/<int:id>')
@api.response(404, 'Student not found')
class Student(Resource):
    @api.doc(description="Retorna um estudante específico")
    def get(self, id):
        student = next((s for s in students if s['id'] == id), None)
        if student is None:
            api.abort(404, "Student not found")
        return student

    @api.doc(description="Atualiza um estudante específico")
    @api.expect(student_model)
    def put(self, id):
        student = next((s for s in students if s['id'] == id), None)
        if student is None:
            api.abort(404, "Student not found")
        student.update(api.payload)
        return student

    @api.doc(description="Deleta um estudante específico")
    def delete(self, id):
        global students
        students = [s for s in students if s['id'] != id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)
