from flask_login import login_required
from flask import render_template, redirect
from . import admin
from app.repository import Repository
from app.entity.Entities import Education

@admin.route('/educations')
@login_required
def educations():
    educations=Education.query.all()
    return render_template('admin/education.html',page='app-mailbox page-aside-left',educations=educations)