from flask_login import login_required, current_user
from flask import render_template, redirect, request, flash, url_for
from . import admin
from app.repository.Repository import repository
from app.entity.Entities import Skill
from .forms import Skill as SkillForm


@admin.route('/skills')
@login_required
def skills():
    form = SkillForm()
    skills = Skill.query.all()
    return render_template('admin/skills/skill.html', form=form, skills=skills, url=url_for('admin.add_skill'))


@admin.route('/skills/add', methods=['POST'])
@login_required
def add_skill():
    form = SkillForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            skill = Skill(skill=form.skill.data, user_id=current_user.id)
            skill.level = form.level.data
            skill.experience = form.experience.data
            skill.percent = form.percent.data
            skill.description = form.description.data
            skill.published = form.published.data
            repository.save(skill)
            flash("Compétence ajoutée avec succès", 'success')
            return redirect(url_for('admin.skills'))
        else:
            flash('Formulaire incorrect', 'error')
    else:
        return redirect(url_for('admin.add_skill'))


@admin.route('/skills/edit/<uid>', methods=['GET', 'POST'])
@login_required
def edit_skill(uid):
    skills = Skill.query.all()
    skill = Skill.query.filter_by(uid=uid).first()
    form = SkillForm(obj=skill)

    if request.method == 'POST':
        if form.validate_on_submit:
            skill.skill = form.skill.data
            skill.level = form.level.data
            skill.experience = form.experience.data
            skill.percent = form.percent.data
            skill.description = form.description.data
            skill.published = form.published.data
            repository.save(skill)
            flash("Compétence modifiée avec succès", 'success')
            return redirect(url_for('admin.skills'))
        else:
            flash('Formulaire incorrect', 'error')
    return render_template('admin/skills/skill.html', form=form, skills=skills, url=url_for('admin.edit_skill', uid=uid), skill=skill)

@admin.route('/skills/delete/<uid>')
@login_required
def delete_skill(uid):
    skill = Skill.query.filter_by(uid=uid).first()
    repository.delete(skill)
    flash("Compétence supprimée avec succès", 'success')
    return redirect(url_for('admin.skills'))
