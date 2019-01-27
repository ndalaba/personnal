from flask import render_template
from . import front
from app.entity.User import User
from app import db

@front.route('/')
def index():
    user = User(name="Diallo Mamadou N'Dalaba",email="dmn@dev-hoster.com")
    user.password="thesniper"
    db.session.add(user)
    db.session.commit()
    return render_template('base.html')