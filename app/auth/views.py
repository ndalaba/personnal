from flask import render_template, request, flash
from datetime import datetime
from . import auth
from app.form.login import LoginForm
from app.entity import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit:
        pass

    return render_template('admin/auth/login.html',form=form, now=datetime.utcnow())
