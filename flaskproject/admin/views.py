from flask import Blueprint, render_template
from flask import current_app, redirect, request, url_for
from flaskproject import db
from flaskproject.users.models import User
from flask_security.decorators import roles_required
from flask_security import login_required, current_user

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
@roles_required('admin')
def index():
    users = [user for user in User.query.all()]
    return render_template('admin/admin_index.html', users=users)