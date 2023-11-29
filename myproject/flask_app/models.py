from flask_app import db

class Form(db.Model):
    firstname = db.Column(db.String(200), primary_key=True)
    lastname = db.Column(db.String(200), nullable=False)