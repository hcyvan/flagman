from kernel.controller import Controller
from repo.user import UserRepo


class User(Controller):
    def register(self):
        nickname = self.json('nickname')
        UserRepo().register(nickname)
        return self.json('nickname')
