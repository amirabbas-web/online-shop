from flask import Flask
from config import *
from extensions import *
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(general)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)