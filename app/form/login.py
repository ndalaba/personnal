# coding: utf-8
# Login form

from flask_wtf import Form
from wtforms import TextField, validators, ValidationError, PasswordField, SubmitField,BooleanField


class LoginForm(Form):
    email = TextField("Email", [validators.Required("Veillez renseigner le champ email"), validators.Email('Renseigner une adresse mail valide')])
    password = PasswordField('Mot de passe', [validators.Required('Veillez renseigner un mot de passe')])
    remember_me= BooleanField('Rester connecté')
    submit = SubmitField('Se connecter')
