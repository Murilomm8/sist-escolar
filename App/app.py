# -*- coding: utf-8 -*-
"""
API de Gestão Escolar - Back-end em Flask (Projeto sis-esco)

Este arquivo implementa uma API RESTful com endpoints para gerenciamento de:
    - Pagamentos
    - Presenças
    - Atividades

A documentação Swagger dos endpoints pode ser acessada em: /api/docs

Utiliza:
  - Flask
  - Flask_SQLAlchemy
  - Flasgger (para Swagger UI)
  
Observação: O SQLite é usado para persistência dos dados.
"""

import os
from datetime import datetime, timezone
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados (SQLite)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'school.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração do Swagger para que a documentação fique acessível em /api/docs
app.config['SWAGGER'] = {
    'title': 'Sis-esco API',
    'uiversion': 3,
    'specs_route': '/api/docs'
}
swagger = Swagger(app)

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# --------------------- MODELOS DE DADOS ---------------------

class Payment(db.Model):
    """
    Modelo para representar um pagamento.

    Attributes:
      id (int): identificador único.
      student_name (str): nome do aluno ou responsável.
      amount (float): valor do pagamento.
      payment_date (datetime): data/hora do pagamento.
      status (str): 'pago' ou 'pendente'.
    """
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default="pendente")

class Attendance(db.Model):
    """
    Modelo para representar um registro de presença.

    Attributes:
      id (int): identificador único.
      student_name (str): nome do aluno.
      date (date): data da presença (formato YYYY-MM-DD).
      present (bool): True se o aluno estava presente.
    """
    id = db.Column(db.Integer, primary_key=True)
    # Utilizamos uma função lambda para evitar o aviso de depreciação,
    # criando um objeto datetime com consciência de fuso horário (UTC)
    date = db.Column(db.Date, nullable=False, default=lambda: datetime.now(timezone.utc).date())
    student_name = db.Column(db.String(100), nullable=False)
    present = db.Column(db.Boolean, nullable=False, default=True)

class Activity(db.Model):
    """
    Modelo para representar uma atividade realizada.

    Attributes:
      id (int): identificador único.
      student_name (str): nome do aluno.
      description (str): descrição da atividade.
      activity_date (datetime): data/hora do registro.
    """
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    activity_date = db.Column(db.DateTime, default=datetime.utcnow)

class Student(db.Model):
    """
    Modelo para representar um aluno.

    Attributes:
      id (int): Identificador único do aluno.
      name (str): Nome do aluno.
      birth_date (date): Data de nascimento do aluno (formato YYYY-MM-DD, opcional).
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)

# --------------------- ROTAS DA API ---------------------

@app.route('/')
def index():
    """
    Rota raiz para verificar se a API está funcionando.
    ---
    tags:
      - Index
    responses:
      200:
        description: Mensagem de status da API.
        examples:
          application/json:
            message: API de Gestão Escolar - Back-end em Flask (Projeto sis-esco)
    """
    return jsonify({'message': 'API de Gestão Escolar - Back-end em Flask (Projeto sis-esco)'}), 200

# ----- Endpoints para Pagamentos -----

@app.route('/payments', methods=['GET'])
def get_payments():
    """
    Lista todos os pagamentos cadastrados.
    ---
    tags:
      - Pagamentos
    responses:
      200:
        description: Lista de pagamentos.
        schema:
          type: array
          items:
            $ref: '#/definitions/Payment'
    definitions:
      Payment:
        type: object
        properties:
          id:
            type: integer
          student_name:
            type: string
          amount:
            type: number
          payment_date:
            type: string
          status:
            type: string
    """
    payments = Payment.query.all()
    results = [
        {
            "id": payment.id,
            "student_name": payment.student_name,
            "amount": payment.amount,
            "payment_date": payment.payment_date.strftime("%Y-%m-%d %H:%M:%S"),
            "status": payment.status
        } for payment in payments
    ]
    return jsonify(results), 200

@app.route('/payments', methods=['POST'])
def create_payment():
    """
    Cria um novo pagamento.
    ---
    tags:
      - Pagamentos
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            student_name:
              type: string
            amount:
              type: number
            status:
              type: string
              default: pendente
    responses:
      201:
        description: Pagamento criado com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
            id:
              type: integer
      400:
        description: Dados insuficientes.
    """
    data = request.get_json()
    if not data or 'student_name' not in data or 'amount' not in data:
        return jsonify({"error": "Dados insuficientes."}), 400

    new_payment = Payment(
        student_name=data['student_name'],
        amount=data['amount'],
        status=data.get('status', 'pendente')
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Pagamento criado com sucesso!", "id": new_payment.id}), 201

# ----- Endpoints para Presenças -----

@app.route('/attendances', methods=['GET'])
def get_attendances():
    """
    Lista registros de presença.
    ---
    tags:
      - Presenças
    parameters:
      - name: student_name
        in: query
        type: string
        description: Filtra por nome do aluno
    responses:
      200:
        description: Lista de registros de presença.
        schema:
          type: array
          items:
            $ref: '#/definitions/Attendance'
    definitions:
      Attendance:
        type: object
        properties:
          id:
            type: integer
          student_name:
            type: string
          date:
            type: string
          present:
            type: boolean
    """
    student_name = request.args.get('student_name')
    query = Attendance.query
    if student_name:
        query = query.filter(Attendance.student_name.ilike(f"%{student_name}%"))
    attendances = query.all()
    results = [
        {
            "id": attendance.id,
            "student_name": attendance.student_name,
            "date": attendance.date.strftime("%Y-%m-%d"),
            "present": attendance.present
        } for attendance in attendances
    ]
    return jsonify(results), 200

@app.route('/attendances', methods=['POST'])
def create_attendance():
    """
    Cria um registro de presença.
    ---
    tags:
      - Presenças
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            student_name:
              type: string
            date:
              type: string
              description: Data da presença no formato YYYY-MM-DD (opcional)
            present:
              type: boolean
              default: true
    responses:
      201:
        description: Presença registrada com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
            id:
              type: integer
      400:
        description: Dados insuficientes ou formato de data inválido.
    """
    data = request.get_json()
    if not data or 'student_name' not in data:
        return jsonify({"error": "Dados insuficientes."}), 400

    if 'date' in data:
        try:
            record_date = datetime.strptime(data['date'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Formato de data inválido. Use YYYY-MM-DD."}), 400
    else:
        record_date = datetime.now(timezone.utc).date()

    new_attendance = Attendance(
        student_name=data['student_name'],
        date=record_date,
        present=data.get('present', True)
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({"message": "Presença registrada com sucesso!", "id": new_attendance.id}), 201

# ----- Endpoints para Atividades -----

@app.route('/activities', methods=['GET'])
def get_activities():
    """
    Lista todas as atividades registradas.
    ---
    tags:
      - Atividades
    parameters:
      - name: student_name
        in: query
        type: string
        description: Filtra por nome do aluno
    responses:
      200:
        description: Lista de atividades.
        schema:
          type: array
          items:
            $ref: '#/definitions/Activity'
    definitions:
      Activity:
        type: object
        properties:
          id:
            type: integer
          student_name:
            type: string
          description:
            type: string
          activity_date:
            type: string
    """
    student_name = request.args.get('student_name')
    query = Activity.query
    if student_name:
        query = query.filter(Activity.student_name.ilike(f"%{student_name}%"))
    activities = query.all()
    results = [
        {
            "id": activity.id,
            "student_name": activity.student_name,
            "description": activity.description,
            "activity_date": activity.activity_date.strftime("%Y-%m-%d %H:%M:%S")
        } for activity in activities
    ]
    return jsonify(results), 200

@app.route('/activities', methods=['POST'])
def create_activity():
    """
    Registra uma nova atividade.
    ---
    tags:
      - Atividades
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            student_name:
              type: string
            description:
              type: string
    responses:
      201:
        description: Atividade registrada com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
            id:
              type: integer
      400:
        description: Dados insuficientes.
    """
    data = request.get_json()
    if not data or 'student_name' not in data or 'description' not in data:
        return jsonify({"error": "Dados insuficientes."}), 400

    new_activity = Activity(
        student_name=data['student_name'],
        description=data['description']
    )
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({"message": "Atividade registrada com sucesso!", "id": new_activity.id}), 201

# ----- Endpoints para Alunos -----
@app.route('/students', methods=['GET'])
def get_students():
    """
    Lista todos os alunos cadastrados.
    ---
    tags:
      - Alunos
    responses:
      200:
        description: Lista de alunos.
        schema:
          type: array
          items:
            $ref: '#/definitions/Student'
    definitions:
      Student:
        type: object
        properties:
          id:
            type: integer
            description: ID único do aluno.
          name:
            type: string
            description: Nome do aluno.
          birth_date:
            type: string
            description: Data de nascimento no formato YYYY-MM-DD.
    """
    students = Student.query.all()
    results = [
        {
            "id": student.id,
            "name": student.name,
            "birth_date": student.birth_date.strftime("%Y-%m-%d") if student.birth_date else None
        } for student in students
    ]
    return jsonify(results), 200

@app.route('/students', methods=['POST'])
def create_student():
    """
    Registra um novo aluno.
    ---
    tags:
      - Alunos
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Nome do aluno.
            birth_date:
              type: string
              description: Data de nascimento no formato YYYY-MM-DD (opcional).
    responses:
      201:
        description: Aluno criado com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
            id:
              type: integer
      400:
        description: Dados insuficientes ou inválidos.
    """
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Dados insuficientes."}), 400

    birth_date = None
    if 'birth_date' in data:
        try:
            birth_date = datetime.strptime(data['birth_date'], "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Formato de data inválido. Use YYYY-MM-DD."}), 400

    new_student = Student(
        name=data['name'],
        birth_date=birth_date
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Aluno criado com sucesso!", "id": new_student.id}), 201


# ----- Endpoint para Reinicializar o Banco de Dados -----
@app.route('/initdb', methods=['GET'])
def init_db():
    """
    Reinicializa o banco de dados removendo e recriando todas as tabelas.
    
    **Atenção:** Use este endpoint somente em ambiente de desenvolvimento, pois todos os dados serão apagados.
    ---
    tags:
      - Banco de Dados
    responses:
      200:
        description: Banco de dados inicializado com sucesso.
        schema:
          type: object
          properties:
            message:
              type: string
    """
    db.drop_all()
    db.create_all()
    return jsonify({"message": "Banco de dados inicializado com sucesso!"}), 200


# --------------------- Inicialização da Aplicação ---------------------

if __name__ == '__main__':
    # Cria as tabelas dentro do contexto da aplicação
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
