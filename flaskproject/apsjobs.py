"""
    flaskproject.apsjobs
    ~~~~~~~~~~~~~~~~
    flaskproject Flask-APScheduler job definitions.
"""

from datetime import datetime
from flask import current_app
from flaskproject import app
from .core import db
from .models import Event


# def job1():
#     # This works.
#     with app.app_context():
#         current_app.logger.info('Flask-APScheduler testing. This runs every 30 seconds.')
#         print('Flask-APScheduler testing. This runs every 30 seconds.')


def events_check():
    with app.app_context():
        # Check for events with status_id 100, active status.
        events = Event.query.filter_by(status_id=100).all()

        for event in events:
            # If the event end_date has expired, change its status_id
            # to 400, completed status.
            if event.end_date <= datetime.utcnow():
                event.status_id = 400
                current_app.logger.info('Event expired. Status updated. Event ID: %s', event.id)

                db.session.add(event)
            else:
                current_app.logger.info('Status 105, no expired events.')


        # Commit the db session back.
        db.session.commit()
