from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command

from db import db
from kernel.app import app

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
