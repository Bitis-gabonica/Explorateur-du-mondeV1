# app.py
from flask import Flask
from models.database import db
from views.routes import register_routes

app = Flask(__name__)
app.secret_key = "devkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///countries.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise SQLAlchemy
db.init_app(app)

# Enregistre les routes définies dans views/routes.py
register_routes(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)