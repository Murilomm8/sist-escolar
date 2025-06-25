PRAGMA foreign_keys = ON;

-- 1) payments
CREATE TABLE IF NOT EXISTS payments (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  student_name  TEXT         NOT NULL,
  amount        REAL         NOT NULL,
  payment_date  DATETIME     DEFAULT CURRENT_TIMESTAMP,
  status        TEXT         NOT NULL DEFAULT 'pendente'
);

-- 2) attendances (presença diária)
CREATE TABLE IF NOT EXISTS attendances (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  student_name  TEXT         NOT NULL,
  date          DATE         DEFAULT CURRENT_DATE,
  present       INTEGER      NOT NULL DEFAULT 1  -- 1 = true, 0 = false
);

-- 3) activities
CREATE TABLE IF NOT EXISTS activities (
  id             INTEGER      PRIMARY KEY AUTOINCREMENT,
  student_name   TEXT         NOT NULL,
  description    TEXT         NOT NULL,
  activity_date  DATETIME     DEFAULT CURRENT_TIMESTAMP
);

-- 4) students
CREATE TABLE IF NOT EXISTS students (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  name          TEXT         NOT NULL,
  birth_date    DATE
);

-- 5) professors
CREATE TABLE IF NOT EXISTS professors (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  name          TEXT         NOT NULL,
  specialty     TEXT         NOT NULL,
  contact       TEXT,
  registry      TEXT         NOT NULL UNIQUE
);

-- 6) disciplines
CREATE TABLE IF NOT EXISTS disciplines (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  name          TEXT         NOT NULL,
  code          TEXT         NOT NULL UNIQUE,
  workload      INTEGER      NOT NULL
);

-- 7) classes (turmas)
CREATE TABLE IF NOT EXISTS classes (
  id            INTEGER      PRIMARY KEY AUTOINCREMENT,
  identifier    TEXT         NOT NULL UNIQUE,
  year          INTEGER      NOT NULL
);

-- 8) class_assignments (turma ↔ disciplina ↔ professor)
CREATE TABLE IF NOT EXISTS class_assignments (
  class_id       INTEGER      NOT NULL,
  discipline_id  INTEGER      NOT NULL,
  professor_id   INTEGER      NOT NULL,
  PRIMARY KEY (class_id, discipline_id),
  FOREIGN KEY (class_id)      REFERENCES classes(id)     ON DELETE CASCADE,
  FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE,
  FOREIGN KEY (professor_id)  REFERENCES professors(id)  ON DELETE SET NULL
);

-- 9) enrollments (matrículas aluno ↔ turma)
CREATE TABLE IF NOT EXISTS enrollments (
  student_id    INTEGER      NOT NULL,
  class_id      INTEGER      NOT NULL,
  PRIMARY KEY (student_id, class_id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (class_id)   REFERENCES classes(id)  ON DELETE CASCADE
);

-- 10) grades (notas por disciplina)
CREATE TABLE IF NOT EXISTS grades (
  student_id     INTEGER     NOT NULL,
  discipline_id  INTEGER     NOT NULL,
  grade          REAL        NOT NULL,
  PRIMARY KEY (student_id, discipline_id),
  FOREIGN KEY (student_id)    REFERENCES students(id)    ON DELETE CASCADE,
  FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE
);

-- 11) academic_attendance (frequência acadêmica por disciplina)
CREATE TABLE IF NOT EXISTS academic_attendance (
  student_id     INTEGER     NOT NULL,
  discipline_id  INTEGER     NOT NULL,
  presences      INTEGER     NOT NULL DEFAULT 0,
  PRIMARY KEY (student_id, discipline_id),
  FOREIGN KEY (student_id)    REFERENCES students(id)    ON DELETE CASCADE,
  FOREIGN KEY (discipline_id) REFERENCES disciplines(id) ON DELETE CASCADE
);

--  
-- Explicação do DDL
--  
-- Este script DDL cria todas as tabelas necessárias para o funcionamento do sistema
-- de gestão escolar Sis-esco, conforme definido no modelo entidade-relacionamento
-- e nas classes ORM do backend Flask/SQLAlchemy.  
--  
-- Principais características:
-- 1. Utiliza PRAGMA foreign_keys = ON para garantir integridade referencial no SQLite.
-- 2. Define chaves primárias (PRIMARY KEY) para unicidade de registros.
-- 3. Estabelece chaves estrangeiras (FOREIGN KEY) com ON DELETE CASCADE/SET NULL, 
--    assegurando que exclusões em tabelas-pai reflitam corretamente nas filhas.
-- 4. Tabelas de associação many-to-many (ex.: class_assignments, enrollments, grades, 
--    academic_attendance) usam chaves compostas como PRIMARY KEY.
--  
-- Como aplicar:
-- - Em ambiente SQLite:  
--     sqlite3 school.db < scripts/ddl.sql  
-- - Em migrations ou SGBD diferente, adapte tipos (TEXT, INTEGER, REAL, DATETIME) 
--   e sintaxe de PRAGMA/ON DELETE conforme o banco alvo (PostgreSQL, MySQL, etc.).  
--  
-- Após rodar este script, todas as tabelas estarão disponíveis e prontas para uso 
-- pela API Flask, garantindo consistência entre o esquema físico e as entidades do código.
--  
