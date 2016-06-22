from flask_security import UserMixin, RoleMixin
from ..core import db

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Role %r>' % (self.name)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(120))
    active = db.Column(db.Boolean())

    last_edit_date = db.Column(db.DateTime())

    # User tracking fields
    # https://pythonhosted.org/Flask-Security/models.html
    #confirmed_at = db.Column(db.DateTime())
    #last_login_at = db.Column(db.DateTime())
    #current_login_at = db.Column(db.DateTime())
    #last_login_ip = db.Column(db.String(100))
    #current_login_ip = db.Column(db.String(100))
    #login_count = db.Column(db.Integer)
    #registered_at = db.Column(db.DateTime())

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
