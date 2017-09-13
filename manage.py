from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command

from kernel.app import app
from model.db import db

manager = Manager(app)
migrate = Migrate(app, db)


class Hello(Command):
    """
    aaa
    """

    def run(self):
        print("hello world")


print(app.url_map)

manager.add_command('hello', Hello())
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
