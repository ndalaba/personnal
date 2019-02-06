from flask import render_template
from . import front
from app.entity.User import User


@front.route('/')
def index():
    user = User.query.filter_by(uid='a6c5a240').first()
    return render_template('base.html', user=user)
