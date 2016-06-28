from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from ..core import db
from flask_security import login_required, current_user
from .models import Event

events = Blueprint('events', __name__, template_folder='templates')

@events.route('/')
@login_required
def index():
    return render_template('events/events.html')
