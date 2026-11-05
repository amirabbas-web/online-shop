from flask import Flask
from config import PORT
from blueprints.general import general

app = Flask(__name__)



app.register_blueprint(general)
if __name__ == "__main__":
    app.run(debug=True, port=PORT)