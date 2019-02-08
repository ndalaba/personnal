from flask import redirect, render_template, flash,url_for
from . import admin
from flask_login import login_required, current_user
from app.entity.Entities import Email
from sqlalchemy import text
from app.repository.Repository import repository

@admin.route('/messages')
@login_required
def messages():
    emails = Email.query.filter_by(user_id=current_user.id).order_by(text('created_at DESC'))[1:15]
    return render_template('admin/messages/index.html',emails=emails)


@admin.route('/messages/nouveau')
@login_required
def compose():
    email = Email(user_id=current_user.id)
    email.email_from=current_user.email
    email.name=current_user.name
    return render_template('admin/messages/compose.html', email=email)


@admin.route('/messages/detail/<uid>')
@login_required
def read(uid):
    email = Email.query.filter_by(user_id=current_user.id,uid=uid).one()
    email.read=True
    repository.save(email)
    return render_template('admin/messages/detail.html',email=email)


@admin.route('/messages/repondre/<uid>')
@login_required
def repondre(uid):
    email = Email.query.filter_by(user_id=current_user.id, uid=uid).one()
    new_mail = Email(user_id=current_user.id)
    new_mail.email_from = current_user.email
    new_mail.email_to=email.email_from
    new_mail.subject = "Re: %s" % email.subject
    return render_template('admin/messages/compose.html', email=new_mail)

@admin.route('/message/supprimer/<uid>')
@login_required
def delete_message(uid):
    email = Email.query.filter_by(user_id=current_user.id, uid=uid).one()
    repository.delete(email)
    flash('Message supprimé','success')
    return redirect(url_for('admin.messages'))
