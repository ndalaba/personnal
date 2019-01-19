from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app =  Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)
login_manager.login_message = "Veillez vous connecter!"
login_manager.login_view = "auth.login"

from app.entity import Job, Service, User, Skill, Work, Education


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/admin')
def admin():
    return render_template('admin/home.html')