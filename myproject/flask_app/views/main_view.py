
from flask import Blueprint, url_for, redirect, render_template, request

from flask_app import db
from flask_app .forms import UserForm
from flask_app.models import Form


bp=Blueprint('main', __name__, url_prefix='/')

#폼화면
@bp.route('/')
def index():
    return render_template('FormPage.html')

@bp.route('/view/', methods=('GET', 'POST'))
def view():
    form=UserForm()
    if request.method=='POST':
        form_user=Form(firstname=form.firstname.data, lastname=form.lastname.data)
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        print("firstname", firstname)
        print("lastname", lastname)
        db.session.add(form_user)
        db.session.commit()
    return render_template('FormView.html', firstname=firstname, lastname=lastname)