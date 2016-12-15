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
    events = Event.query.filter_by(user_id=current_user.id)

    return render_template('events/events.html', events=events)


@events.route('/')
@login_required
def display_events():
    events = Event.query.filter_by(user_id=current_user.id)

    return render_template("events/events.html", events=events)


@events.route('/create', methods=['GET', 'POST'])
@login_required
def create_event():
    form = NewEventForm(request.form)

    if request.method == 'POST' and form.validate():
        address = form.address.data
        address_line_two = form.address_line_two.data
        category_id = 100
        city = form.city.data
        country = form.country.data
        end_date = form.end_date.data
        last_edit_date = datetime.utcnow()
        name = form.name.data
        start_date = form.start_date.data
        state = form.state.data
        status_id = 100
        user_id = current_user.id
        zip_code = form.zip_code.data
        event = Event(address, address_line_two, category_id, city, country, end_date, last_edit_date, name,
                      start_date, state, status_id, user_id, zip_code)

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
        event.address = form.address.data
        event.address_line_two = form.address_line_two.data
        event.city = form.city.data
        event.country = form.country.data
        event.end_date = form.end_date.data
        event.last_edit_date = datetime.utcnow()
        event.name = form.name.data
        event.start_date = form.start_date.data
        event.zip_code = form.zip_code.data

        try:
            db.session.commit()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

        return redirect(url_for('events.show', event_id=event.id))
    elif request.method != "POST":
        form.address.data = event.address
        form.address_line_two.data = event.address_line_two
        form.city.data = event.city
        form.country.data = event.country
        form.end_date.data = event.end_date
        form.name.data = event.name
        form.start_date.data = event.start_date
        form.zip_code.data = event.zip_code

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
