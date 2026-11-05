from flask import Flask
from config import PORT
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True, port=PORT)