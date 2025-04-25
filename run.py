from app import create_app
from app import db  # Importando o db para garantir a inicialização do banco

# Cria a aplicação
app = create_app()

# Inicia o servidor
if __name__ == '__main__':
    # Aqui você pode definir o host e a porta desejada
    app.run(host='0.0.0.0', port=5000, debug=True)

# Definição do modelo de Turma
class Turma(db.Model):
    __tablename__ = 'turma'

    # Definindo os campos da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)

    # Método construtor para facilitar a criação de objetos de turma
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

    def __repr__(self):
        return f"<Turma {self.nome} - {self.periodo}>"
