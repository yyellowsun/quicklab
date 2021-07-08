from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from serverapi.application import create_app
from serverapi.models import db, User, Work

app=create_app()

migrate=Migrate(app,db)
manager =Manager(app)

manager.add_command('db',MigrateCommand)

@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                User=User,
                Work=Work
    )

if __name__ == '__main__':
    manager.run()