from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class UserForm(FlaskForm):
    name = StringField('Nome do usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired()])
    password_hash = PasswordField('Insira sua senha:', validators=[DataRequired(), EqualTo('password_hash2', message='As senhas precisam ser iguais!')])
    password_hash2 = PasswordField('Confirmar senha:', validators=[DataRequired()])
    submit = SubmitField('Enviar')