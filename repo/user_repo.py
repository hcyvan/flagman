from model.db import User, db
from werkzeug.security import generate_password_hash, check_password_hash


def create(nickname, phone, password):
    password_hash = generate_password_hash(password)
    user = {
        "nickname": nickname,
        "phone": phone,
        "password_hash": password_hash,
    }
    db.session.add(User(**user))
    db.session.commit()


def get_user_by_phone(phone):
    return User.query.filter_by(phone=phone).first()


def check_user_password(user, password):
    return check_password_hash(user.password_hash, password)


def is_nickname_used(nickname):
    return User.query.filter_by(nickname=nickname).count() > 0


def is_phone_used(phone):
    return User.query.filter_by(phone=phone).count() > 0
