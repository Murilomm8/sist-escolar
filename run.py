from app import create_app

# Cria a aplicação
app = create_app()

# Inicia o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

class Turma(db.Model):
    __tablename__ = 'turma'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo
