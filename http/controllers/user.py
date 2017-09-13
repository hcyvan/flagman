from kernel.controller import Controller
from repo import user


class User(Controller):
    def register(self):
        nickname = self.json('nickname')
        phone = self.json('phone')
        password = self.json('password')
        user.add(nickname, phone, password)
        return self.echo()
