from flaskproject import app
from flaskproject.core import db
from flaskproject.events.models import Event, Category, Status

def populate_status():
    status_active = Status(name='active', status_code=100)
    status_inactive = Status(name='inactive', status_code=200)

    db.session.add(status_active)
    db.session.add(status_inactive)
    db.session.commit()

with app.app_context():

    populate_status()
