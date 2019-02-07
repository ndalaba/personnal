from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_message = "Veillez vous connecter!"
login_manager.login_view = "auth.login"

from .entity import Job, Service, User, Skill, Work, Education

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from .front import front as front_blueprint

app.register_blueprint(front_blueprint)
