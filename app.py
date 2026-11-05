from flask import Flask
from config import PORT
from blueprints.general import general
from blueprints.admin import admin
from blueprints.user import user
app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(admin)
app.register_blueprint(general)
if __name__ == "__main__":
    app.run(debug=True, port=PORT)