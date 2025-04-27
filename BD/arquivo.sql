
---

### 2. **BD**  
Esta pasta contém arquivos relacionados à configuração do banco de dados. Neste exemplo, o back-end utiliza SQLAlchemy com SQLite. O diretório BD serve de placeholder caso seja necessário migrar para outro SGBD ou para documentar o DDL.

---

#### **sis-esco/BD/arquivo.sql**

```sql
-- DDL para criação das tabelas do sistema de gestão escolar.
-- Este script é um exemplo para SQLite; adapte conforme o SGBD utilizado.

-- Tabela Payment
CREATE TABLE IF NOT EXISTS Payment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(100) NOT NULL,
    amount REAL NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL DEFAULT 'pendente'
);

-- Tabela Attendance
CREATE TABLE IF NOT EXISTS Attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(100) NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    present BOOLEAN NOT NULL DEFAULT 1
);

-- Tabela Activity
CREATE TABLE IF NOT EXISTS Activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    activity_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
