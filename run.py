from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tabled():
    db.create_all()