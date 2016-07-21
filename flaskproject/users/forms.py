# -*- coding: utf-8 -*-
"""
    flaskproject.users.forms
    ~~~~~~~~~~~~~~~~~~~~~
    User forms
"""

from flask_wtf import Form
from wtforms import StringField, DateField, DateTimeField
from wtforms import validators

class EditProfileForm(Form):
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=30)
    ])
    first_name = StringField('First Name', [validators.Length(min=1, max=70)])
    last_name = StringField('Last Name', [validators.Length(min=1, max=70)])
    birthdate = DateField('Birth Date', [validators.DataRequired()], format='%m-%d-%Y')
    # birthdate = DateTimeField('Birth Date', format='%m/%d/%Y %I:%M:%S %p')
    # birthdate = DateField('Birth Date', format='%Y-%m-%d')
