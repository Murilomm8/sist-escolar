-- Criação do banco de dados
CREATE DATABASE sistema_escolar_db;

-- Seleção do banco de dados para as operações
\c sistema_escolar_db;

-- Tabela para armazenar as informações de usuários
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,  -- "admin", "aluno", "professor"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela para armazenar os alunos
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    data_nascimento DATE,
    endereco VARCHAR(255),
    telefone VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabela para armazenar os professores
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    especialidade VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabela para armazenar as turmas
CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    periodo VARCHAR(50),
    turno VARCHAR(50),  -- "manha", "tarde", "noite"
    ano INT
);

-- Tabela para armazenar as matérias
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT
);

-- Tabela para armazenar a relação entre turmas e matérias
CREATE TABLE class_subjects (
    class_id INT NOT NULL,
    subject_id INT NOT NULL,
    PRIMARY KEY (class_id, subject_id),
    FOREIGN KEY (class_id) REFERENCES classes(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);

-- Tabela para armazenar a relação entre alunos e turmas
CREATE TABLE student_classes (
    student_id INT NOT NULL,
    class_id INT NOT NULL,
    PRIMARY KEY (student_id, class_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (class_id) REFERENCES classes(id)
);

-- Tabela para armazenar as notas dos alunos
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    grade DECIMAL(5,2),  -- Nota com duas casas decimais
    data DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
);
