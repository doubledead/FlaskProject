from flask_wtf import Form
from wtforms import StringField, DateField
from wtforms.fields import DateField, DateTimeField
# from wtforms.validators import DataRequired
from wtforms import validators

class CreateEventForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=70)])
    address = StringField('Address', [validators.Length(min=1, max=70)])
