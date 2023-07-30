
# Settings

DEBUG = True
# Setting TESTING to True disables @login_required checks
TESTING = False

CACHE_TYPE = 'simple'

## SQLite Connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
# Local PostgreSQL Connection
# SQLALCHEMY_DATABASE_URI = 'postgresql://puser:Password1@localhost/devdb1'
SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39a'

# Flask-Mail
# Required for Flask-Security registration to function properly
MAIL_DEFAULT_SENDER = 'info@flaskproject.us'
MAIL_SERVER = 'smtp.postmarkapp.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

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


# Flask-APScheduler
# JOBS = [
#     {
#         'id': 'job1',
#         'func': 'flaskproject.apsjobs:events_check',
#         'trigger': 'interval',
#         'seconds': 30
#     }
# ]
# SCHEDULER_VIEWS_ENABLED = True
