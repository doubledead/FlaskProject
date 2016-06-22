from wtforms import Form, TextField, TextAreaField, validators

class CreateEventForm(Form):
    title = TextField('Title', [validators.Length(min=1, max=70)])
    body = TextAreaField('Body', [validators.Length(min=1, max=300)])
