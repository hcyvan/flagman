from model.db import User, db
from werkzeug.security import generate_password_hash, check_password_hash


def add(nickname, phone, password):
    # # todo something
    password_hash = generate_password_hash(password)
    user = {
        "nickname": nickname,
        "phone": phone,
        "password_hash": password_hash,
    }
    db.session.add(User(**user))
    db.session.commit()


def check_by_phone(phone, password):
    password_hash = ''
    return check_password_hash(password_hash, password)


def is_nickname_used(nickname):
    return User.query.filter_by(nickname=nickname).count() > 0


def is_phone_used(phone):
    return User.query.filter_by(phone=phone) > 0
