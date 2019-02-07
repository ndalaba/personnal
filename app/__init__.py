from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
<<<<<<< HEAD
=======
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
<<<<<<< HEAD
=======
toolbar = DebugToolbarExtension(app)
mail = Mail(app)
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99

login_manager = LoginManager(app)
login_manager.login_message = "Veillez vous connecter!"
login_manager.login_view = "auth.login"

<<<<<<< HEAD
from .entity import Job, Service, User, Skill, Work, Education
=======
from .entity.Entities import Job, Service, Skill, Work, Education, Hobby,Activity
from .entity.User import User
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99

from .admin import admin as admin_blueprint

app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

from .front import front as front_blueprint

app.register_blueprint(front_blueprint)
<<<<<<< HEAD
=======


from app.utils.filter import datetimeformat
app.jinja_env.filters['datetimeformat'] = datetimeformat
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99
