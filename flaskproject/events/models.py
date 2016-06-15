from flaskproject import db
from datetime import datetime

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225))
    create_date = db.Column(db.DateTime())

    def __init__(self, name=None, create_date=None):
        self.name = name
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date

    def __repr__(self):
        return '<Event %r>' % (self.name)
