import random

from flask import render_template, url_for, jsonify, redirect, request

from app.entity.Entities import Email
from app.entity.User import User
from app.repository.Repository import repository
from . import front
from .form import EmailForm
from flask_mail import Message
from app import mail


@front.route('/')
def index():
    colors = ['blue.css', 'brown.css', 'cyan.css', 'gray.css']
    user = User.query.filter_by(uid='a6c5a240').first()
    color = url_for('static', filename="css/colors/" + random.choice(colors))
    form = EmailForm()
    return render_template('front/base.html', user=user, color=color, form=form)


@front.route('/contact', methods=['POST'])
def contact():
    form = EmailForm()
    if request.method == 'POST':
        if form.is_submitted():
            user = User.query.filter_by(uid=form.user.data).first()
            if user is None:
                return jsonify(type="error", text="Erreur formulaire.")
            email = Email(user_id=user.id)
            email.email_from = form.email.data
            email.folder = "INBOX"
            email.email_to = user.email
            email.subject = form.subject.data
            email.message = form.message.data
            email.name = form.name.data
            repository.save(email)
            
            msg = Message(email.subject, sender=(email.name,email.email_from), recipients=[user.email])
            msg.body = email.message
            mail.send(msg)

            return jsonify(type="success", text="Votre message a été envoyé.")
        return jsonify(type="error", text="Erreur formulaire.")
    return redirect(url_for('front.index'))
