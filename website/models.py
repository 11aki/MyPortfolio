from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    portf = db.relationship('Portfolio')


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True) #needs to be here
    asset = db.Column(db.String(10000))
    asset_type = db.Column(db.String(10000)) 
    bought = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    date_bought = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    


