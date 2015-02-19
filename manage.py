from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from project import app, db
from project.allowance import allowance

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

manager.add_command("give_allowance", allowance.GiveAllowance())

manager.add_command("mike_is_rich", allowance.MikeIsRich())

manager.add_command("delete_users", allowance.DeleteUsers())

manager.add_command("create_users", allowance.CreateUsers())

if __name__ == '__main__':
    manager.run()