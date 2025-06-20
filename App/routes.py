from flask import Blueprint, request, jsonify
from flasgger import swag_from
from datetime import datetime, timezone
from models import (
    db, Payment, Attendance, Activity, Student,
    Professor, Discipline, SchoolClass,
    Enrollment, Grade, AcademicAttendance,
    ClassAssignment
)

bp = Blueprint('api', __name__)

#
#  Utilitários comuns
#
def not_found_response(entity, _id):
    return jsonify({"error": f"{entity} com id={_id} não encontrado."}), 404

#
# 1) Pagamentos (Payment)
#
@bp.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([p.__dict__ for p in payments]), 200

@bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json() or {}
    if 'student_name' not in data or 'amount' not in data:
        return jsonify({"error": "Dados insuficientes."}), 400
    p = Payment(
        student_name=data['student_name'],
        amount=data['amount'],
        status=data.get('status','pendente')
    )
    db.session.add(p); db.session.commit()
    return jsonify({"message":"Criado","id":p.id}), 201

@bp.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    p = Payment.query.get(id)
    if not p: return not_found_response("Payment", id)
    data = request.get_json() or {}
    for attr in ('student_name','amount','status'):
        if attr in data: setattr(p,attr,data[attr])
    db.session.commit()
    return jsonify({"message":"Atualizado"}), 200

@bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    p = Payment.query.get(id)
    if not p: return not_found_response("Payment", id)
    db.session.delete(p); db.session.commit()
    return jsonify({"message":"Deletado"}), 200

#
# 2) Presenças (Attendance)
#
@bp.route('/attendances', methods=['GET'])
def get_attendances():
    q = Attendance.query
    name = request.args.get('student_name')
    if name: q = q.filter(Attendance.student_name.ilike(f"%{name}%"))
    return jsonify([a.__dict__ for a in q.all()]), 200

@bp.route('/attendances', methods=['POST'])
def create_attendance():
    data = request.get_json() or {}
    if 'student_name' not in data:
        return jsonify({"error":"Dados insuficientes"}), 400
    att = Attendance(
        student_name=data['student_name'],
        present=data.get('present',True),
        date=datetime.strptime(data['date'], '%Y-%m-%d').date() if data.get('date') else None
    )
    db.session.add(att); db.session.commit()
    return jsonify({"message":"Criado","id":att.id}),201

@bp.route('/attendances/<int:id>', methods=['PUT'])
def update_attendance(id):
    a = Attendance.query.get(id)
    if not a: return not_found_response("Attendance", id)
    data=request.get_json() or {}
    if 'present' in data: a.present=data['present']
    if 'date' in data:
        a.date=datetime.strptime(data['date'],'%Y-%m-%d').date()
    db.session.commit()
    return jsonify({"message":"Atualizado"}),200

@bp.route('/attendances/<int:id>', methods=['DELETE'])
def delete_attendance(id):
    a=Attendance.query.get(id)
    if not a: return not_found