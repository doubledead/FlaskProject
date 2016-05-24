from flask import abort, Flask, g, render_template, request
from flask_mail import Mail
from flask_security import current_user
from flaskproject.utils import get_instance_folder_path
from flaskproject.main.controllers import main
from flaskproject.admin.controllers import admin
from flaskproject.user.controllers import user
from flaskproject.cache import cache
from flaskproject.config import configure_app
from flaskproject.data.models import db

app = Flask(__name__,
            instance_path=get_instance_folder_path(),
            instance_relative_config=True,
            template_folder='templates')

configure_app(app)
cache.init_app(app)

#: Flask-Mail extension instance
mail = Mail()

db.init_app(app)
mail.init_app(app)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path, error))
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return render_template('500.html'), 500

@app.context_processor
def inject_user():
    return dict(user=current_user)

@app.route('/')
@cache.cached(300)
def home():
    return render_template('index.html')

app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
