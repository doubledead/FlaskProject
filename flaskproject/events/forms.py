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
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=1, max=250)
    ])
    address = StringField('Address', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    address_line_two = StringField('Line 2', [validators.Length(max=70)])
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
    country = StringField('Country', [validators.Length(max=70)
    ])
    # start_date = DateTimeField('Start Date', [validators.DataRequired()], format='%m-%d-%Y %H:%M')
    # start_date = DateTimeField('Start Date', [validators.DataRequired()])
    start_date = StringField('Start Date', [validators.DataRequired()])
    # end_date = DateTimeField('End Date', [validators.DataRequired()], format='%m-%d-%Y %H:%M')
    # end_date = DateTimeField('End Date', [validators.DataRequired()])
    end_date = StringField('End Date', [validators.DataRequired()])

class UpdateEventForm(Form):
    name = StringField('Name', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    address = StringField('Address', [
        validators.DataRequired(),
        validators.Length(min=1, max=70)
    ])
    address_line_two = StringField('Line 2', [validators.Length(max=70)])
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
    start_date = DateTimeField('Start Date', [validators.DataRequired()], format='%m-%d-%Y %H:%M')
    end_date = DateTimeField('End Date', [validators.DataRequired()], format='%m-%d-%Y ')
