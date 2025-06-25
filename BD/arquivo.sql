-- DDL para todas as entidades do Sis-esco

PRAGMA foreign_keys = ON;

-- 1) Payments
CREATE TABLE IF NOT EXISTS payments (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name  TEXT    NOT NULL,
    amount        REAL    NOT NULL,
    payment_date  DATETIME DEFAULT CURRENT_TIMESTAMP,
    status        TEXT    NOT NULL DEFAULT 'pendente'
);

-- 2) Attendances
CREATE TABLE IF NOT EXISTS attendances (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name  TEXT    NOT NULL,
    date          DATE    DEFAULT CURRENT_DATE,
    present       INTEGER NOT NULL DEFAULT 1  -- 1 = true, 0 = false
);

-- 3) Activities
CREATE TABLE IF NOT EXISTS activities (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name   TEXT    NOT NULL,
    description    TEXT    NOT NULL,
    activity_date  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 4) Students
CREATE TABLE IF NOT EXISTS students (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    birth_date   DATE
);

-- 5) Professors
CREATE TABLE IF NOT EXISTS professors (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    name             TEXT    NOT NULL,
    specialty        TEXT    NOT NULL,
    contact          TEXT,
    registry         TEXT    NOT NULL UNIQUE
);

-- 6) Disciplines
CREATE TABLE IF NOT EXISTS disciplines (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL,
    code         TEXT    NOT NULL UNIQUE,
    workload     INTEGER NOT NULL
);

-- 7) Classes (Turmas)
CREATE TABLE IF NOT EXISTS classes (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    identifier    TEXT    NOT NULL UNIQUE,
    year          INTEGER NOT NULL
);

-- 8) ClassAssignments (Disciplina ↔ Turma ↔ Professor)
CREATE TABLE IF NOT EXISTS class_assignments (
    class_id       INTEGER NOT NULL,
    discipline_id  INTEGER NOT NULL,
    professor_id   INTEGER NOT NULL,
    PRIMARY KEY (class_id, discipline_id),
    FOREIGN KEY (class_id)      REFERENCES classes(id)     ON DELETE CASCADE,
    FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE,
    FOREIGN KEY (professor_id)  REFERENCES professors(id)  ON DELETE SET NULL
);

-- 9) Enrollments (Matrículas)
CREATE TABLE IF NOT EXISTS enrollments (
    student_id   INTEGER NOT NULL,
    class_id     INTEGER NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id)   REFERENCES classes(id)  ON DELETE CASCADE
);

-- 10) Grades (Notas)
CREATE TABLE IF NOT EXISTS grades (
    student_id     INTEGER NOT NULL,
    discipline_id  INTEGER NOT NULL,
    grade          REAL    NOT NULL,
    PRIMARY KEY (student_id, discipline_id),
    FOREIGN KEY (student_id)    REFERENCES students(id)    ON DELETE CASCADE,
    FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE
);

-- 11) AcademicAttendance (Frequência por Disciplina)
CREATE TABLE IF NOT EXISTS academic_attendance (
    student_id     INTEGER NOT NULL,
    discipline_id  INTEGER NOT NULL,
    presences      INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (student_id, discipline_id),
    FOREIGN KEY (student_id)    REFERENCES students(id)    ON DELETE CASCADE,
    FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE
);
