
from models.database import db
from datetime import datetime

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(3), unique=True, nullable=False)
    capital = db.Column(db.String(100))
    region = db.Column(db.String(100))
    flag_url = db.Column(db.String(300))
    languages = db.Column(db.String(200))
    currency = db.Column(db.String(100))
    timezone = db.Column(db.String(100))
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Country {self.name}>"
