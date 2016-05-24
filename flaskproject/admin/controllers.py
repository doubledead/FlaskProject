from flask import Blueprint, render_template
from flask import current_app, redirect, request, url_for
from flask_security.decorators import roles_required, current_user
from flaskproject.data.models import db, User
from sqlalchemy import exc


admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
@roles_required('admin')
def index():
    users = [user for user in User.query.all()]
    return render_template('admin_index.html', users=users)