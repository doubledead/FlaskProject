# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~
    Manager module
"""

from flask.ext.script import Manager

from flaskproject import app
from flaskproject.core import db
from flaskproject.events.models import Event, Category, Status

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()
