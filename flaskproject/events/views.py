from flask import Blueprint, render_template
from flask import request, redirect, url_for, json, current_app
from flaskproject import db
from flask_security import login_required, current_user
from flaskproject.events.models import Event

mod = Blueprint('events', __name__, template_folder='templates')

@mod.route('/')
@login_required
def index():
    return render_template('events/events.html')