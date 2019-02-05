from flask import render_template
from . import front
from app.entity.User import User
from app import db

@front.route('/')
def index():
    return render_template('base.html')