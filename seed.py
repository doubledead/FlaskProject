from flaskproject import create_app
from flaskproject.core import db

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
