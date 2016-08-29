from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from ..core import db
from flask_security import login_required, current_user
from datetime import datetime
from .forms import NewEventForm, UpdateEventForm
from .models import Event, Category, Status, Guest
from sqlalchemy import exc

events = Blueprint('events', __name__, template_folder='templates')

@events.route('/')
@login_required
def index():
    user_id = current_user.id
    events = Event.query.filter_by(user_id=user_id)

    return render_template('events/events.html', events=events)

@events.route('/')
@login_required
def display_events():
    user_id = current_user.id
    events = Event.query.filter_by(user_id=user_id)

    return render_template("events/events.html", events=events)

@events.route('/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = NewEventForm(request.form)

    if request.method == 'POST' and form.validate():
        title = form.title.data
        address = form.address.data
        city = form.city.data
        state = form.state.data
        zip_code = form.zip_code.data
        country = form.country.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        last_edit_date = datetime.utcnow()
        user_id = current_user.id
        category = Category(name='active', status_code=100)
        status = Status(name='active', status_code=100)
        event = Event(title, address, city, state, zip_code, country,
                      start_date, end_date, last_edit_date, user_id, status, category)

        try:
            db.session.add(event)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('events.display_events'))

    return render_template("events/create_event.html", form=form)

@events.route('/<event_id>', methods=['GET', 'POST'])
@login_required
def show(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()

    guests = event.guests

    return render_template("events/show.html", event=event, guests=guests)

@events.route('/update/<event_id>', methods=['GET', 'POST'])
@login_required
def update(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()

    form = UpdateEventForm()
    if request.method == "POST" and form.validate():
        event.title = form.title.data
        event.address = form.address.data
        event.start_date = form.start_date.data
        event.end_date = form.end_date.data
        event.last_edit_date = datetime.utcnow()

        try:
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('events.show', event_id=event.id))
    elif request.method != "POST":
        form.title.data = event.title
        form.address.data = event.address
        form.start_date.data = event.start_date
        form.end_date.data = event.end_date

    return render_template("events/update.html", event=event, form=form)

@events.route('/delete/<event_id>', methods=['GET', 'POST'])
@login_required
def delete(event_id):
    event = Event.query.filter_by(id=event_id).first_or_404()
    user_id = current_user.id
    if user_id == event.user_id:
        try:
            db.session.delete(event)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('events.display_events'))

    return redirect(url_for('events.display_events'))
