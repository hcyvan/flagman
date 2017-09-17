from kernel.controller import Controller
from repo import user_repo


class User(Controller):
    def register(self):
        nickname = self.json('nickname')
        phone = self.json('phone')
        password = self.json('password')

        if user_repo.is_phone_used(phone):
            return self.echo(101)
        if user_repo.is_nickname_used(nickname):
            return self.echo(102)
        try:
            user_repo.create(nickname, phone, password)
        except Exception:
            return self.echo(1)
        else:
            return self.echo()

    def login(self):
        phone = self.json('phone')
        password = self.json('password')

        user = user_repo.get_user_by_phone(phone)
        if not user:
            return self.echo(103)

        if user_repo.check_user_password(user, password):
            # TODO: JWT token返回
            return self.echo()
        else:
            return self.echo(104)

