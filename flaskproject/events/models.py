from ..core import db
from datetime import datetime


events_invitees = db.Table(
    'events_invitees',
    db.Column('invitee_id', db.Integer(), db.ForeignKey('invitees.id')),
    db.Column('event_id', db.Integer(), db.ForeignKey('events.id')))

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225))
    description = db.Column(db.String(225))


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225))
    create_date = db.Column(db.DateTime())

    category_id = db.Column(db.ForeignKey('categories.id'))
    category = db.relationship('Category',
                               backref=db.backref('events', lazy='dynamic'))

    invitees = db.relationship('Invitee',
                               secondary=events_invitees,
                               backref=db.backref('events', lazy='dynamic'))

    def __init__(self, category, name=None, create_date=None):
        self.name = name
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date
        self.category = category

    def __repr__(self):
        return '<Event %r>' % (self.name)

class Invitee(db.Model):
    __tablename__ = 'invitees'

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer(), db.ForeignKey('events.id'))
    email_address = db.Column(db.String(225))
    status = db.Column(db.Integer())
