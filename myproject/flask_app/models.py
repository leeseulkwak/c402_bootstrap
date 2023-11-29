from flask_app import db

class Form(db.Model):
    firstname = db.Column(db.String(200), primary_key=True)
    lastname = db.Column(db.String(200), nullable=False)
    cars = db.Column(db.String(200), nullable=True)
    fav_language = db.Column(db.String(200), nullable=True)
    create_date = db.Column(db.DateTime(), nullable=True)