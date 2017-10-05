import datetime
from flask_sqlalchemy import SQLAlchemy

from kernel.app import app

db = SQLAlchemy(app)


def models_to_matrix(models):
    return [model.to_dict() for model in models]


class BaseModel(db.Model):
    __abstract__ = True
    create_at = db.Column(db.DateTime, default=datetime.datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    delete_at = db.Column(db.DateTime)

    def update(self, except_none=True,**kw):
        for k, v in kw.items():
            if getattr(self, k):
                if except_none and v is None:
                    continue
                setattr(self, k, v)
        db.session.commit()

    def to_dict(self):
        column_name_list = [value[0] for value in self._sa_instance_state.attrs.items()]
        return dict((column_name, getattr(self, column_name, None)) for column_name in column_name_list)


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