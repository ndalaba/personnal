from flask import render_template,flash,redirect,url_for,request
from flask_login import login_required, current_user
from . import admin
from app.admin.forms import UserForm
from app.repository.Repository import repository
from app.utils.upload import uploadImage
from app.entity.Activity import Activity


@admin.route('/home')
@admin.route('/')
@login_required
def home():
    return render_template('admin/home.html',page='dashboard')


@admin.route('activities/<uid>',methods=['POST','GET'])
@login_required
def activities(uid=None):
    if request.method=='POST':
        description=request.form['activity']
        activity= Activity(description=description,user_id=current_user.id)
        repository.save(activity)
        flash('Activité ajoutée avec succès','success')
    else: #suppression
        activity= Activity.query.filter_by(uid=uid).first()
        repository.delete(activity)
        flash('Activité supprimée avec succès','success')
       
    return redirect(url_for('admin.profil'))

@admin.route('/profils')
def profil():
    activities=Activity.query.order_by(Activity.created_at.desc())
    return render_template('admin/profil.html',page='page-profile',activities=activities)


@admin.route('/edit_profil', methods=['GET','POST'])
@login_required
def edit_profil():

    form= UserForm(obj=current_user)
    
    if request.method=='POST': 
        if form.validate_on_submit:
            if form.photo.data and form.photo.data!=current_user.photo:
                image = uploadImage(form.photo.data,'admin/upload/')
                current_user.photo= image

            current_user.name=form.name.data
            current_user.email=form.email.data
            current_user.phone=form.phone.data
            current_user.job=form.job.data
            current_user.facebook=form.facebook.data
            current_user.twitter=form.twitter.data
            current_user.github=form.github.data
            current_user.linkedin=form.linkedin.data
            current_user.bio=form.bio.data
            current_user.location=form.location.data
            repository.save(current_user)
            flash('Compte mis à jour avec succès','success')
            return redirect(url_for('admin.profil'))
        
        else:
            flash('Les champs du formulaire ne sont pas bien remplis','error')
    
    return render_template('admin/edit_profil.html', page='page-profile',form=form)
