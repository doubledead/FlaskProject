from wtforms import Form, TextField, TextAreaField, validators

class CreateEntryForm(Form):
  title = TextField('Title', [validators.Length(min=1, max=70)])
  body = TextAreaField('Body', [validators.Length(min=1, max=300)])