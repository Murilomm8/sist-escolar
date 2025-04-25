# -*- coding: utf-8 -*-
"""
API de Gestão Escolar - Back-end em Flask

Projeto: sis-esco

Este arquivo implementa uma API RESTful com endpoints para gerenciamento de:
    - Pagamentos
    - Presenças
    - Atividades

Utiliza Flask e Flask_SQLAlchemy com SQLite para persistência de dados.
Cada rota possui comentários que auxiliam na compreensão e manutenção do código.
"""

import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados: este exemplo utiliza SQLite para facilitar testes locais.
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'school.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# --------------------- MODELOS DE DADOS ---------------------

class Payment(db.Model):
    """
    Modelo para representar um pagamento.
    Atributos:
        id: identificador único.
        student_name: nome do aluno ou responsável associado ao pagamento.
        amount: valor pago.
        payment_date: data/hora do pagamento.
        status: status do pagamento ('pago' ou 'pendente').
    """
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default="pendente")

class Attendance(db.Model):
    """
    Modelo para representar um registro de presença.
    Atributos:
        id: identificador único.
        student_name: nome do aluno.
        date: data da presença (YYYY-MM-DD).
        present: booleano indicando se o aluno esteve presente.
    """
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date())
    present = db.Column(db.Boolean, nullable=False, default=True)

class Activity(db.Model):
    """
    Modelo para representar uma atividade realizada por um aluno.
    Atributos:
        id: identificador único da atividade.
        student_name: nome do aluno.
        description: descrição da atividade (ex.: desenho, tarefa).
        activity_date: data/hora do registro.
    """
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    activity_date = db.Column(db.DateTime, default=datetime.utcnow)

# --------------------- ROTAS DA API ---------------------

@app.route('/')
def index():
    """
    Rota raiz para verificar se a API está funcionando.
    Retorna uma mensagem simples.
    """
    return jsonify({'message': 'API de Gestão Escolar - Back-end em Flask (Projeto sis-esco)'}), 200

# ----- Endpoints para Pagamentos -----

@app.route('/payments', methods=['GET'])
def get_payments():
    """
    GET /payments
    Retorna uma lista de todos os pagamentos cadastrados.
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
    POST /payments
    Cria um registro de pagamento.
    Espera receber um JSON com:
      - student_name: nome do aluno ou responsável.
      - amount: valor do pagamento.
      - status: opcional, 'pago' ou 'pendente' (padrão 'pendente').
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
    GET /attendances
    Retorna registros de presença.
    Permite filtrar por 'student_name' via parâmetros de query.
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
    POST /attendances
    Registra a presença de um aluno.
    Espera receber um JSON com:
      - student_name: nome do aluno.
      - date: opcional, data da presença (YYYY-MM-DD); se não informado, usa a data atual.
      - present: opcional, booleano indicando presença (padrão True).
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
        record_date = datetime.utcnow().date()
    
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
    GET /activities
    Retorna registro de atividades.
    Permite filtrar por 'student_name' via query.
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
    POST /activities
    Registra uma nova atividade realizada por um aluno.
    Espera receber um JSON com:
      - student_name: nome do aluno.
      - description: descrição da atividade.
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

# ----- Endpoint para Inicializar o Banco de Dados -----

@app.route('/initdb', methods=['GET'])
def init_db():
    """
    GET /initdb
    Reinicializa o banco de dados: remove todas as tabelas existentes e recria.
    ATENÇÃO: Utilize este endpoint somente em ambiente de desenvolvimento, pois apaga todos os dados!
    """
    db.drop_all()   # Remove todas as tabelas
    db.create_all() # Cria as tabelas conforme os modelos definidos
    return jsonify({"message": "Banco de dados inicializado com sucesso!"}), 200

# --------------------- Inicialização da Aplicação ---------------------

if __name__ == '__main__':
    # Cria as tabelas se não existirem
    db.create_all()
    # Inicia o servidor Flask (debug ativo e acessível em todas as interfaces na porta 5000)
    app.run(debug=True, host='0.0.0.0')
