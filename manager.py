from flask_migrate import MigrateCommand
from flask_script import Manager
from app import creat_app
app = creat_app('development')
manage=Manager(app)
manage.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manage.run()
