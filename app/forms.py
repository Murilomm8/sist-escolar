from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

class UserForm(FlaskForm):
    # Campo para o nome de usuário com validação de preenchimento obrigatório
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])

    # Campo para a senha com validação de preenchimento obrigatório
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

    # Confirmação de senha, para garantir que o usuário digite corretamente
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])

    # Campo para o papel/funcão do usuário (Admin, Usuário, etc.)
    role = StringField('Role', validators=[DataRequired(), Length(min=3, max=50)])

    # A validade de email também pode ser adicionada se necessário
    # email = StringField('Email', validators=[DataRequired(), Email()])
