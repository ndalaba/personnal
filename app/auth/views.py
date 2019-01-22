from flask import render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_login import login_user
from . import auth
from .form import LoginForm
from app.entity.User import User


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('admin.index'))
        else:
            flash('Email ou mot de passe incorrect')

    return render_template('admin/auth/login.html', form=form, now=datetime.utcnow())
