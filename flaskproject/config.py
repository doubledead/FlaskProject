# from flaskproject import db
# from flaskproject.data.models import db, Role, User
# from flaskproject.users.models import Role, User
# from flask_security import Security, SQLAlchemyUserDatastore
# import os
# import logging
#
#
# class BaseConfig(object):
#     DEBUG = False
#     TESTING = False
#     # sqlite :memory: identifier is the default if no filepath is present
#     SQLALCHEMY_DATABASE_URI = 'sqlite://'
#     SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0a'
#     LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     LOGGING_LOCATION = 'flaskproject.log'
#     LOGGING_LEVEL = logging.DEBUG
#     CACHE_TYPE = 'simple'
#
#      # Flask-Mail
#      # Required for Flask-Security registration to function properly
#     MAIL_DEFAULT_SENDER = 'info@flaskproject.us'
#     MAIL_SERVER = 'smtp.postmarkapp.com'
#     MAIL_PORT = 25
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = 'username'
#     MAIL_PASSWORD = 'password'
#
#     # Flask-Security
#     SECURITY_CONFIRMABLE = False
#     SECURITY_REGISTERABLE = True
#     SECURITY_POST_LOGIN_VIEW = '/main'
#     SECURITY_POST_LOGOUT_VIEW = '/'
#     SECURITY_POST_REGISTER_VIEW = '/main'
#     SECURITY_SEND_REGISTER_EMAIL = False
#
#
# class DevelopmentConfig(BaseConfig):
#     DEBUG = True
#     # Setting TESTING to True disables @login_required checks
#     TESTING = False
#     # Linux SQLite reference
#     #SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
#     # PostgreSQL Connection
#     SQLALCHEMY_DATABASE_URI = 'postgresql://puser:Password1@localhost/devdb'
#     SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39a'
#
#
# class TestingConfig(BaseConfig):
#     DEBUG = False
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite://'
#     SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faaa'
#
# config = {
#     "development": "flaskproject.config.DevelopmentConfig",
#     "testing": "flaskproject.config.TestingConfig",
#     "default": "flaskproject.config.DevelopmentConfig"
# }
#
#
# def configure_app(app):
#     config_name = os.getenv('FLAKS_CONFIGURATION', 'default')
#     app.config.from_object(config[config_name]) # object-based default configuration
#     app.config.from_pyfile('config.cfg', silent=True) # instance-folders configuration
#     # Configure logging
#     handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
#     handler.setLevel(app.config['LOGGING_LEVEL'])
#     formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
#     handler.setFormatter(formatter)
#     app.logger.addHandler(handler)
#     # Configure Security
#     # user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#     # app.security = Security(app, user_datastore)
