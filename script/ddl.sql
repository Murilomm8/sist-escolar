CREATE TABLE alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    data_nascimento DATE,
    endereco VARCHAR(255),
    contato_responsavel VARCHAR(255),
    matricula VARCHAR(50) UNIQUE
);

CREATE TABLE professores (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    especialidade VARCHAR(255),
    contato VARCHAR(255),
    registro_profissional VARCHAR(50) UNIQUE
);

CREATE TABLE disciplinas (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    codigo VARCHAR(50) UNIQUE,
    carga_horaria INT
);

CREATE TABLE turmas (
    id INT PRIMARY KEY,
    identificacao VARCHAR(50) UNIQUE,
    ano_letivo INT
);

CREATE TABLE matriculas (
    id_aluno INT,
    id_turma INT,
    PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_turma) REFERENCES turmas(id)
);

CREATE TABLE notas (
    id_aluno INT,
    id_disciplina INT,
    nota DECIMAL(4,2),
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
);

CREATE TABLE frequencia (
    id_aluno INT,
    id_disciplina INT,
    presencas INT,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id)
);
/*Sistema de Gestão Escolar - Modelo Relacional
1. Introdução
Este documento tem como objetivo explicar a estrutura do banco de dados relacional criado para um sistema de gestão escolar. O modelo proposto foi elaborado utilizando o conceito de Modelo Entidade-Relacionamento (MER) e posteriormente convertido em um DDL (Data Definition Language) para a criação física do banco de dados.

2. Entidades e Tabelas
O banco de dados é composto por várias tabelas que representam as diferentes entidades do sistema. A seguir, detalhamos cada uma delas.

2.1. Tabela alunos
Finalidade: Armazena as informações dos alunos cadastrados no sistema.

Atributos:

id (INT, PRIMARY KEY): Identificador único de cada aluno.

nome (VARCHAR(255)): Nome completo do aluno.

data_nascimento (DATE): Data de nascimento.

endereco (VARCHAR(255)): Endereço do aluno.

contato_responsavel (VARCHAR(255)): Contato dos pais ou responsáveis.

matricula (VARCHAR(50), UNIQUE): Código de matrícula único.

2.2. Tabela professores
Finalidade: Registra os professores cadastrados no sistema.

Atributos:

id (INT, PRIMARY KEY): Identificador único do professor.

nome (VARCHAR(255)): Nome completo.

especialidade (VARCHAR(255)): Área de atuação do professor.

contato (VARCHAR(255)): Informações de contato.

registro_profissional (VARCHAR(50), UNIQUE): Número de registro profissional.

2.3. Tabela disciplinas
Finalidade: Registra as disciplinas oferecidas na instituição.

Atributos:

id (INT, PRIMARY KEY): Identificador único da disciplina.

nome (VARCHAR(255)): Nome da disciplina.

codigo (VARCHAR(50), UNIQUE): Código identificador da disciplina.

carga_horaria (INT): Quantidade de horas destinadas à disciplina.

2.4. Tabela turmas
Finalidade: Identifica as turmas existentes, agrupando alunos e disciplinas.

Atributos:

id (INT, PRIMARY KEY): Identificador único da turma.

identificacao (VARCHAR(50), UNIQUE): Nome ou código da turma.

ano_letivo (INT): Ano correspondente à turma.

2.5. Tabela matriculas
Finalidade: Relaciona alunos às turmas em que estão matriculados.

Atributos:

id_aluno (INT, FOREIGN KEY para alunos.id): Identifica o aluno.

id_turma (INT, FOREIGN KEY para turmas.id): Identifica a turma.

Constraints:

PRIMARY KEY (id_aluno, id_turma): Impede duplicação de matrículas para o mesmo aluno/turma.

FOREIGN KEY (id_aluno) REFERENCES alunos(id): Garante que um aluno matriculado existe na tabela alunos.

FOREIGN KEY (id_turma) REFERENCES turmas(id): Garante que a turma matriculada existe na tabela turmas.

2.6. Tabela notas
Finalidade: Registra as notas dos alunos em cada disciplina.

Atributos:

id_aluno (INT, FOREIGN KEY para alunos.id): Identifica o aluno.

id_disciplina (INT, FOREIGN KEY para disciplinas.id): Disciplina correspondente.

nota (DECIMAL(4,2)): Nota obtida pelo aluno na disciplina.

Constraints:

PRIMARY KEY (id_aluno, id_disciplina): Evita registros duplicados de notas do mesmo aluno para a mesma disciplina.

FOREIGN KEY (id_aluno) REFERENCES alunos(id): Garante a existência do aluno na tabela alunos.

FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id): Garante que a disciplina registrada existe.

2.7. Tabela frequencia
Finalidade: Armazena o número de presenças dos alunos em cada disciplina.

Atributos:

id_aluno (INT, FOREIGN KEY para alunos.id): Identifica o aluno.

id_disciplina (INT, FOREIGN KEY para disciplinas.id): Disciplina correspondente.

presencas (INT): Número total de presenças do aluno na disciplina.

Constraints:

PRIMARY KEY (id_aluno, id_disciplina): Evita registros duplicados de presença do mesmo aluno para a mesma disciplina.

FOREIGN KEY (id_aluno) REFERENCES alunos(id): Garante que o aluno registrado existe na tabela alunos.

FOREIGN KEY (id_disciplina) REFERENCES disciplinas(id): Garante que a disciplina registrada existe.

3. Conclusão
Este banco de dados foi projetado para garantir a integridade e a organização das informações relacionadas à gestão escolar. A definição das chaves primárias (PK) assegura unicidade dos registros, enquanto as chaves estrangeiras (FK) reforçam a integridade referencial, garantindo que os dados estejam sempre consistentes.

Além disso, a estrutura relacional utilizada melhora a escalabilidade do sistema e facilita consultas futuras para relatórios e análises. Caso haja necessidade de expansão, novas tabelas podem ser adicionadas para contemplar outros aspectos do sistema, como a gestão de horários, avaliações e comunicação entre alunos e professores.