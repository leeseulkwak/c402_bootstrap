
from flask import Blueprint, url_for, redirect, render_template, request
from werkzeug.utils import redirect, secure_filename

from flask_app import db
from flask_app .forms import UserForm
from flask_app.models import Form
from datetime import datetime
import os

import config
# now=datetime.datetime.now()

bp=Blueprint('main', __name__, url_prefix='/')


# 파일을 저장하기
def save_file(file):
    try:
        filename = secure_filename(file.filename)
        current_time = datetime.utcnow()
        unique_filename = f"{current_time.strftime('%Y%m%d%H%M%S')}_{filename}"

        # 년도와 월을 포함하는 디렉토리 경로 생성
        year_month_path = os.path.join(config.UPLOAD_FOLDER, current_time.strftime('%Y/%m'))

        # 해당 경로가 존재하지 않으면 생성
        if not os.path.exists(year_month_path):
            os.makedirs(year_month_path)

        filepath = os.path.join(year_month_path, unique_filename)
        file.save(filepath)
        return unique_filename
    except Exception as e:
        # 에러 처리 (로그 기록 등)
        return None


#폼화면
@bp.route('/')
def index():
    return render_template('FormPage.html')

@bp.route('/view/', methods=('GET', 'POST'))
def view():
    form=UserForm()
    if request.method=='POST':

        f = form.file.data
        # 첨부파일이 있는 경우 저장하고 없으면 None
        filename = save_file(f) if f else None
        
        form_user=Form(firstname=form.firstname.data, lastname=form.lastname.data, cars=form.cars.data, 
                       fav_language=form.fav_language.data, create_date=datetime.now(), filename=filename)
        firstname=request.form.get("firstname")
        lastname=request.form.get("lastname")
        cars=request.form.get("cars")
        fav_language=request.form.get("fav_language")
        filename=request.form.get("filename")

        db.session.add(form_user)
        db.session.commit()
        return render_template('FormView.html', firstname=firstname, lastname=lastname, cars=cars, fav_language=fav_language, filename=filename )

# # 첨부파일 추가하기
# @bp.route('/upload/', methods=('GET', 'POST'))
# def file_upload():
#     form = UserForm()
#     if request.method == 'POST' and form.validate_on_submit():
#         f = form.file.data
#         # 첨부파일이 있는 경우 저장하고 없으면 None
#         filename = save_file(f) if f else None

#         name = Form(first_name=form.fname.data, last_name=form.lname.data, create_date=datetime.now(), filename=filename)
#         db.session.add(name)
#         db.session.commit()
#         return redirect(url_for('/'))
#     return render_template('Upload.html', form=form)