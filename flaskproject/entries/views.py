from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from flaskproject import db
from flask_security import login_required, current_user
from flaskproject.entries.forms.entry_forms import CreateEntryForm
from flaskproject.cache import cache
from flaskproject.entries.models import Entry

entries = Blueprint('entries', __name__, template_folder='templates')

@mod.route('/')
@login_required
def index():
    entries = [entry for entry in Entry.query.all()]
    current_app.logger.info('Displaying all entries.')

    return render_template('entries/entries.html')

#@main.route('/entries/')
@login_required
@cache.cached(300)
def display_entries():
    entries = [entry for entry in Entry.query.all()]
    current_app.logger.info('Displaying all entries.')

    return render_template("entries/entries.html", entries=entries)

@main.route('/create', methods=['GET', 'POST'])
@login_required
def create_entry():
    form = CreateEntryForm(request.form)
    user_id = current_user.id

    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data
        user_id = user_id
        current_app.logger.info('Adding a new entry %s.', (title))
        entry = Entry(title, body, user_id)

        try:
            db.session.add(entry)
            db.session.commit()
            cache.clear()
        except exc.SQLAlchemyError as e:
            current_app.logger.error(e)

            return redirect(url_for('entries.create_entry'))

        return redirect(url_for('entries.display_entries'))

    return render_template("entries/create_entry.html", form=form)