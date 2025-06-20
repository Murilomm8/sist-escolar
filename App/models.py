from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Associação Classe ↔ Disciplina ↔ Professor
class ClassAssignment(db.Model):
    __tablename__ = 'class_assignments'
    class_id      = db.Column(db.Integer, db.ForeignKey('classes.id'),   primary_key=True)
    discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), primary_key=True)
    professor_id  = db.Column(db.Integer, db.ForeignKey('professors.id'),  nullable=False)
    # Relacionamentos (opcionais)
    classe       = db.relationship('SchoolClass', back_populates='assignments')
    discipline   = db.relationship('Discipline', back_populates='assignments')
    professor    = db.relationship('Professor', back_populates='assignments')

class Payment(db.Model):
    __tablename__ = 'payments'
    id            = db.Column(db.Integer,   primary_key=True)
    student_name  = db.Column(db.String(100), nullable=False)
    amount        = db.Column(db.Float,      nullable=False)
    payment_date  = db.Column(db.DateTime,   default=datetime.utcnow)
    status        = db.Column(db.String(20), nullable=False, default='pendente')

class Attendance(db.Model):
    __tablename__ = 'attendances'
    id            = db.Column(db.Integer,    primary_key=True)
    student_name  = db.Column(db.String(100), nullable=False)
    date          = db.Column(db.Date,       nullable=False, 
                              default=lambda: datetime.now(timezone.utc).date())
    present       = db.Column(db.Boolean,    nullable=False, default=True)

class Activity(db.Model):
    __tablename__ = 'activities'
    id            = db.Column(db.Integer,   primary_key=True)
    student_name  = db.Column(db.String(100), nullable=False)
    description   = db.Column(db.Text,      nullable=False)
    activity_date = db.Column(db.DateTime,  default=datetime.utcnow)

class Student(db.Model):
    __tablename__ = 'students'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    birth_date    = db.Column(db.Date,      nullable=True)

class Professor(db.Model):
    __tablename__ = 'professors'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    specialty     = db.Column(db.String(100), nullable=False)
    contact       = db.Column(db.String(100), nullable=True)
    registry      = db.Column(db.String(50),  unique=True, nullable=False)
    assignments   = db.relationship('ClassAssignment', back_populates='professor')

class Discipline(db.Model):
    __tablename__ = 'disciplines'
    id            = db.Column(db.Integer,   primary_key=True)
    name          = db.Column(db.String(100), nullable=False)
    code          = db.Column(db.String(50),  unique=True, nullable=False)
    workload      = db.Column(db.Integer,    nullable=False)
    assignments   = db.relationship('ClassAssignment', back_populates='discipline')

class SchoolClass(db.Model):
    __tablename__ = 'classes'
    id            = db.Column(db.Integer, primary_key=True)
    identifier    = db.Column(db.String(50), unique=True, nullable=False)
    year          = db.Column(db.Integer, nullable=False)
    assignments   = db.relationship('ClassAssignment', back_populates='classe')

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    student_id    = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    class_id      = db.Column(db.Integer, db.ForeignKey('classes.id'),  primary_key=True)
    student       = db.relationship('Student', backref='enrollments')
    classe        = db.relationship('SchoolClass', backref='enrollments')

class Grade(db.Model):
    __tablename__ = 'grades'
    student_id    = db.Column(db.Integer, db.ForeignKey('students.id'),    primary_key=True)
    discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), primary_key=True)
    grade         = db.Column(db.Float,   nullable=False)
    student       = db.relationship('Student',    backref='grades')
    discipline    = db.relationship('Discipline', backref='grades')

class AcademicAttendance(db.Model):
    __tablename__ = 'academic_attendance'
    student_id    = db.Column(db.Integer, db.ForeignKey('students.id'),    primary_key=True)
    discipline_id = db.Column(db.Integer, db.ForeignKey('disciplines.id'), primary_key=True)
    presences     = db.Column(db.Integer, nullable=False, default=0)
    student       = db.relationship('Student',    backref='academic_attendance')
    discipline    = db.relationship('Discipline', backref='academic_attendance')
