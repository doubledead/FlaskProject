from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from ..core import db
from flask_security.decorators import roles_required
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

@user.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    form = EditProfileForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        last_edit_date = datetime.utcnow()
        current_app.logger.info('Saving profile information for %s.', (email))
        user = User(email, password, last_edit_date)

        try:
            db.session.add(user)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

            return redirect(url_for('edit'))
    else:
        form.email.data = current_user.email
        form.password.data = current_user.password

    return render_template('users/edit_profile.html', form=form)
