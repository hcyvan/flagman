from flask_script import Manager, Command
from flask_migrate import Migrate, MigrateCommand

from app import app
from db import db, User

manager = Manager(app)
migrate = Migrate(app, db)


class Hello(Command):
    """
    aaa
    """

    def run(self):
        print("hello world")


manager.add_command('hello', Hello())
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
