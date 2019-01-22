from flask import render_template
from . import front

@front.route('/')
def index():
    return render_template('base.html')