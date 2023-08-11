import os
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


DEBUG = True
# Setting TESTING to True disables @login_required checks
TESTING = False

CACHE_TYPE = 'simple'

SECRET_KEY = getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

# Flask-Mail
# Required for Flask-Security registration to function properly
MAIL_DEFAULT_SENDER = 'info@flaskproject.us'
MAIL_SERVER = 'smtp.postmarkapp.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = getenv("MAIL_PASSWORD")

# Flask-Security
SECURITY_CONFIRMABLE = False
SECURITY_CHANGEABLE = True
SECURITY_REGISTERABLE = True
SECURITY_POST_CHANGE_VIEW = '/user'
SECURITY_POST_LOGIN_VIEW = '/main'
SECURITY_POST_LOGOUT_VIEW = '/'
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False # Prod change
SECURITY_POST_REGISTER_VIEW = '/main'
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_SALT = 'Some_salt'
SECURITY_EMAIL_SENDER = 'test@test.com'

# Configure logging
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
