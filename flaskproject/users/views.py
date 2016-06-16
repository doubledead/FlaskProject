from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
# from flaskproject import db
from ..core import db
from flask_security.decorators import roles_required
from flask_security import login_required, current_user
# from flaskproject.users.models import User, Role
from .models import User, Role

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
@login_required
def index():
    return render_template('users/user_profile.html')
