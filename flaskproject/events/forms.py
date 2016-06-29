from flask_wtf import Form
from wtforms import StringField
# from wtforms.validators import DataRequired
from wtforms import validators
# from wtforms import Form, TextField, TextAreaField, validators

class CreateEventForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=70)])
