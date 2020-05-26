from project.app import app
from project.db import db

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()
