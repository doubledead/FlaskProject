# -*- coding: utf-8 -*-
"""
    flaskproject.events.forms
    ~~~~~~~~~~~~~~~~~~~~~
    Event forms
"""


from flask_wtf import Form
from wtforms import StringField, DateField, DateTimeField
from wtforms import validators

class NewEventForm(Form):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    address = StringField('Address', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    city = StringField('City', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    state = StringField('State', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    zip_code = StringField('Zip Code', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    country = StringField('Country', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    start_date = DateField('Start Date', [validators.DataRequired()], format='%m-%d-%Y')
    end_date = DateField('End Date', [validators.DataRequired()], format='%m-%d-%Y')

class UpdateEventForm(Form):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    address = StringField('Address', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    city = StringField('City', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    state = StringField('State', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    zip_code = StringField('Zip Code', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    country = StringField('Country', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    start_date = DateField('Start Date', [validators.DataRequired()], format='%m-%d-%Y')
    end_date = DateField('End Date', [validators.DataRequired()], format='%m-%d-%Y')
