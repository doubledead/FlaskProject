from flask_wtf import Form
# from wtforms import Form, TextField, TextAreaField, validators
# from flask_wtf import Form, TextField, Required
from wtforms import StringField, PasswordField
from wtforms import validators

class EditProfileForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=30)])
    # first_name = TextField('First Name', [validators.Length(min=1, max=70)])
    # last_name = TextField('Last Name', [validators.Length(min=1, max=70)])
    # username = TextField('Username', [validators.Length(min=1, max=70)])
    # password = PasswordField('Password', [validators.Length(min=1, max=70)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match.')
    ])
    confirm = PasswordField('Repeat Password')
