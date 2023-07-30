from flask_apscheduler import APScheduler
from flask_moment import Moment
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security


db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()
moment = Moment()
scheduler = APScheduler()
security = Security()
