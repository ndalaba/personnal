from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextField, validators, TextAreaField,SubmitField


class UserForm(Form):
    name= TextField('Nom et prénom',[validators.Required('Veillez renseigner le champ nom et prénom')])
    email= TextField('Email',[validators.Required('Veillez renseigner le champ email'),validators.Email('Champ email incorrect')])
    phone= TextField('Téléphone',[validators.Required('Veillez renseigner le champ téléphone')])
    job= TextField('Fonction',[validators.Required('Veillez renseigner le champ fonction')])
    facebook= TextField('Facebook')
    twitter= TextField('Twitter')
    github= TextField('Github')
    linkedin= TextField('Linkedin')
    location= TextAreaField('Adresse')
    bio= TextAreaField('Biographie')
    photo= FileField('Photo',validators=[FileAllowed(['jpg','jpeg','png'])])
    submit= SubmitField('Valider')