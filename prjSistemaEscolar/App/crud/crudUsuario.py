from app.models import Usuario, db

def create_usuario(nome, email, senha):
    usuario = Usuario(nome=nome, email=email, senha=senha)
    db.session.add(usuario)
    db.session.commit()

def get_usuario_by_id(id):
    return Usuario.query.get(id)

def get_all_usuarios():
    return Usuario.query.all()

def update_usuario(id, nome, email, senha):
    usuario = Usuario.query.get(id)
    if usuario:
        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha
        db.session.commit()

def delete_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
