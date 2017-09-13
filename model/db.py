import datetime
from flask_sqlalchemy import SQLAlchemy

from kernel.app import app

db = SQLAlchemy(app)


class BaseModel(db.Model):
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    delete_at = db.Column(db.DateTime)


class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(48), index=True)
    phone = db.Column(db.String(48), index=True)
    password_hash = db.Column(db.String(128), index=True)
    sex = db.Column(db.SmallInteger)


class Flag(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.Text())
    address = db.Column(db.String(256))
    people_number = db.Column(db.Integer)
    start_time = db.Column(db.DateTime)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
