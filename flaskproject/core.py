# -*- coding: utf-8 -*-

# core module

from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security

#: Flask-SQLAlchemy extension instance
db = SQLAlchemy()

#: Flask-Mail extension instance
mail = Mail()

#: Flask-Security extension instance
security = Security()
