from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms import validators
# from wtforms import TextField, TextAreaField, validators

class CreateEntryForm(Form):
    # title = TextField('Title', [validators.Length(min=1, max=70)])
    title = StringField('Title', [validators.Length(min=1, max=70)])
    body = TextAreaField('Body', [validators.Length(min=1, max=300)])

class UpdateEntryForm(Form):
    # title = TextField('Title', [validators.Length(min=1, max=70)])
    title = StringField('Title', [validators.Length(min=1, max=70)])
    body = TextAreaField('Body', [validators.Length(min=1, max=300)])
