from flask import Flask
from config import *
from extensions import *
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from models.User import User
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY

app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(general)
db.init_app(app)

csrf = CSRFProtect()
csrf.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).filter()

if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)