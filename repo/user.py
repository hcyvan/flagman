from model.db import User, db


class UserRepo:
    def register(self, nickname: str, phone: str, password: str, salt: str) -> str:
        # # todo something
        user = {
            "nickname": nickname,
            "phone": phone
        }
        db.session.add(User(**user))
        db.session.commit()
        return nickname
