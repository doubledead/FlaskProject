from flaskproject import app
from flaskproject.core import db
from flaskproject.events.models import Event, Category, Status

def populate_status():
    status_active = Status(name='active')
    status_inactive = Status(name='inactive')

    category_event = Category('event')

    db.session.add(status_active)
    db.session.add(status_inactive)

    db.session.add(category_event)
    # db.session.commit()

with app.app_context():

    populate_status()
    db.session.commit()
