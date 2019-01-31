from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed
from wtforms import TextField, validators, TextAreaField,SubmitField,DateField, BooleanField


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

class Education(Form):
    formation= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    location= TextField('Lieu',[validators.Required('Veillez renseigner le champ lieu')])
    school= TextField('Etablissement',[validators.Required('Veillez renseigner le champ établissement')])
    begin_at= DateField('Début',[validators.Required('Veillez renseigner le champ début')])
    end_at= DateField('Fin',[validators.Required('Veillez renseigner le champ fin')])
    description= TextAreaField('Description')
    published= BooleanField('Publié')

class Job(Form):
    title= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    location= TextField('Lieu',[validators.Required('Veillez renseigner le champ lieu')])
    company= TextField('Entreprise',[validators.Required('Veillez renseigner le champ entreprise')])
    begin_at= DateField('Début',[validators.Required('Veillez renseigner le champ début')])
    end_at= DateField('Fin',[validators.Required('Veillez renseigner le champ fin')])
    description= TextAreaField('Description')
    published= BooleanField('Publié')

class Service(Form):
    service= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    icon= TextField('Icon',[validators.Required('Veillez renseigner le champ icon')])
    description= TextAreaField('Description')
    details= TextAreaField('Détails')
    published= BooleanField('Publié')

class Hobby(Form):
    service= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    icon= TextField('Icon',[validators.Required('Veillez renseigner le champ icon')])
    description= TextAreaField('Description')
    published= BooleanField('Publié')

class Skill(Form):
    skill= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    level= TextField('Niveau',[validators.Required('Veillez renseigner le champ niveau')])
    experience= TextField("Année d'expérience",[validators.Required("Veillez renseigner le champ année d'expérience")])
    percent= TextField('Pourcentage')
    description= TextAreaField('Description')
    published= BooleanField('Publié')

class Work(Form):
    title= TextField('Titre',[validators.Required('Veillez renseigner le champ titre')])
    techno= TextField('Technologie',[validators.Required('Veillez renseigner le champ technologie')])
    url= TextField('Lien')
    image= FileField('Image',validators=[FileAllowed(['jpg','jpeg','png'])])
    published= BooleanField('Publié')