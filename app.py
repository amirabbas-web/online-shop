from flask import Flask
from config import *
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(general)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=PORT)