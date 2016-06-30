from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from ..core import db
from flask_security import login_required, current_user
from .forms import CreateEventForm
from flaskproject.cache import cache
from .models import Event
from sqlalchemy import exc

events = Blueprint('events', __name__, template_folder='templates')

@events.route('/')
@login_required
def index():
    events = [event for event in Event.query.all()]
    current_app.logger.info('Displaying all entries.')

    return render_template('events/events.html', events=events)

@events.route('/')
@login_required
def display_events():
    events = [event for event in Event.query.all()]
    current_app.logger.info('Displaying all entries.')

    return render_template("events/events.html", events=events)

@events.route('/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = CreateEventForm(request.form)
    user_id = current_user.id

    if request.method == 'POST' and form.validate():
        title = form.title.data
        address = form.address.data
        user_id = user_id
        current_app.logger.info('Adding a new entry %s.', (title))
        event = Event(title, address, user_id)

        try:
            db.session.add(event)
            db.session.commit()
            cache.clear()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('events.display_events'))

    return render_template("events/create_event.html", form=form)
