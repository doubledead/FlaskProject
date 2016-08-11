from flask import Blueprint, render_template, flash
from flask import request, redirect, url_for, json, current_app
from ..core import db
from flask_security import login_required, current_user
from datetime import datetime
from .forms import EditProfileForm
from .models import User, Role
from sqlalchemy import exc

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
@login_required
def index():
    return render_template('users/user_profile.html')

@user.route('/<user_id>', methods=['GET', 'POST'])
@login_required
def show(user_id):
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first_or_404()

    return render_template('users/user_profile.html', user=user)

@user.route('/edit', methods=['GET', 'POST'])
@login_required
def update():
    user_id = current_user.id
    user = User.query.filter_by(id=user_id).first_or_404()
    form = EditProfileForm()

    if request.method == "POST" and form.validate():
        user.email = form.email.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.last_edit_date = datetime.utcnow()

        try:
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('user.show', user_id=user.id))
    elif request.method != "POST":
        form.email.data = user.email
        form.last_name.data = user.last_name
        form.first_name.data = user.first_name

    return render_template('users/edit_profile.html', form=form)
