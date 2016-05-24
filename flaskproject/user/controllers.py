from flask import Blueprint, render_template, flash
from flask import current_app, redirect, request, url_for, json
from flask_security.decorators import roles_required
from flask_security import login_required, current_user
from flaskproject.data.models import db
from sqlalchemy import exc


user = Blueprint('user', __name__, template_folder='templates')


@user.route('/')
@login_required
def index():
    return render_template('user_profile.html')

@user.route('/test', methods=['POST'])
@login_required
def display_test():
	#data = request.json

	#fname = data.get("fName")
	#lname = data.get("lName")
	#email = data.get("email")
	return json.dumps({'status':'OK', 'fname':'John', 'lname':'Smith', 'dateOfBirth':'Coming soon', 'email':'john@smith.com'})