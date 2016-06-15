from flaskproject import db
from datetime import datetime

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(300))
    create_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, body, user_id, create_date=None):
        self.title = title
        self.body = body
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date
        self.user_id = user_id

    def __repr__(self):
      return '<Entry %r>' % self.title