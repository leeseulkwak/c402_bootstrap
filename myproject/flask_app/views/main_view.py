
from flask import Blueprint, url_for, redirect, render_template, request

from flask_app import db
from flask_app .forms import UserForm
from flask_app.models import Form
from datetime import datetime

# now=datetime.datetime.now()

bp=Blueprint('main', __name__, url_prefix='/')

#폼화면
@bp.route('/')
def index():
    return render_template('FormPage.html')

@bp.route('/view/', methods=('GET', 'POST'))
def view():
    form=UserForm()
    if request.method=='POST':
        form_user=Form(firstname=form.firstname.data, lastname=form.lastname.data, cars=form.cars.data, 
                       fav_language=form.fav_language.data, create_date=datetime.now())
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        cars=request.form.get("cars")
        fav_language=request.form.get("fav_language")

        db.session.add(form_user)
        db.session.commit()
    return render_template('FormView.html', firstname=firstname, lastname=lastname, cars=cars, fav_language=fav_language )