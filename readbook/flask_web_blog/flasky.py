"""
Created by catleer on 2018-09-08.
"""
__author__ = 'catleer'

import sys
sys.path.append('.')

import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.models import User, Role, Permission

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# manager = Manager(app)
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission)

# manager.add_command('shell', Shell(make_context=make_shell_context()))
# manager.add_command('db', MigrateCommand)

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# if __name__ == '__main__':
#     app.run()
