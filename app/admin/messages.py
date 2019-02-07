from flask import redirect, render_template
from . import admin
from flask_login import login_required, current_user

@admin.route('/messages')
@login_required
def messages():
    return render_template('admin/messages/index.html')


@admin.route('/messages/nouveau')
@login_required
def compose():
    return render_template('admin/messages/compose.html')


@admin.route('/messages/detail')
@login_required
def read():
    return render_template('admin/messages/detail.html')
