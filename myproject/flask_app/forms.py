from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserForm(FlaskForm):
    firstname= StringField('firstname', validators=[DataRequired(), Length(min=3, max=25)])
    lastname = StringField('lastname', validators=[DataRequired(), Length(min=3, max=25)])
