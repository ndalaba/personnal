from flask import render_template
from . import front

@front.route('/home')
def index():
    return render_template('base.html')