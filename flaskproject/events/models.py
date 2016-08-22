from ..core import db
from datetime import datetime


events_guests = db.Table(
    'events_guests',
    db.Column('event_id', db.Integer(), db.ForeignKey('events.id')),
    db.Column('guest_id', db.Integer(), db.ForeignKey('guests.id')))

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(225))

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return 'Guest %r>' % (self.email)


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(225))
    address = db.Column(db.String(225))
    city = db.Column(db.String(225))
    state = db.Column(db.String(225))
    zip_code = db.Column(db.String(225))
    country = db.Column(db.String(225))
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    last_edit_date = db.Column(db.DateTime())
    create_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Status and Category - Simple Relationship
    # http://flask-sqlalchemy.pocoo.org/2.1/quickstart/
    status_id = db.Column(db.ForeignKey('status.id'))
    status = db.relationship('Status',
                             backref=db.backref('events', lazy='dynamic'))

    category_id = db.Column(db.ForeignKey('category.id'))
    category = db.relationship('Category',
                               backref=db.backref('events', lazy='dynamic'))

    # Many-to-Many
    # https://github.com/mattupstate/overholt/blob/master/overholt/products/models.py
    guests = db.relationship('Guest', secondary=events_guests,
                           backref=db.backref('events', lazy='joined'))

    def __init__(self, title, address, city, state, zip_code, country,
                 start_date, end_date, last_edit_date, user_id, status,
                 category, create_date=None):
        self.title = title
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.start_date = start_date
        self.end_date = end_date
        self.last_edit_date = last_edit_date
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date
        self.user_id = user_id
        self.status = status
        self.category = category

    def __repr__(self):
        return '<Event %r>' % (self.title)

class Category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225))
    description = db.Column(db.String(225))
    status_code = db.Column(db.Integer())

    def __init__(self, name, description, status_code):
        self.name = name
        self.description = description
        self.status_code = status_code

        def __repr__(self):
            return 'Category %r>' % self.name

class Status(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(225))
    description = db.Column(db.String(225))
    status_code = db.Column(db.Integer())

    def __init__(self, name, description, status_code):
        self.name = name
        self.description = description
        self.status_code = status_code

        def __repr__(self):
            return 'Status %r>' % self.name
