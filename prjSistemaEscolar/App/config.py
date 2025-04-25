import os

class Config:
    # URL do banco de dados PostgreSQL (se estiver usando Docker ou ambiente específico, a URL pode ser diferente)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://root:123456@localhost:5432/')
    
    # Desabilita a notificação de alterações de objetos para economizar recursos
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração adicional para a aplicação Flask (por exemplo, chaves secretas)
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave_secreta_default')  # Defina uma chave secreta para sessões e CSRF
    
    # Outras configurações, se necessário
    # Exemplo: se você quiser permitir a exibição de logs de erros
    # DEBUG = os.getenv('FLASK_DEBUG', True)

