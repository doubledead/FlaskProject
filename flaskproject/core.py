# -*- coding: utf-8 -*-

# core module

from flask_apscheduler import APScheduler
from flask.ext.moment import Moment
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security

#: Flask-SQLAlchemy extension instance
db = SQLAlchemy()

ma = Marshmallow()

#: Flask-Mail extension instance
mail = Mail()

#: Moment.js integration within Jinja2
# https://blog.miguelgrinberg.com/post/flask-moment-flask-and-jinja2-integration-with-momentjs
moment = Moment()

# Flask-APScheduler extension instance
# https://github.com/viniciuschiele/flask-apscheduler
scheduler = APScheduler()

#: Flask-Security extension instance
security = Security()
