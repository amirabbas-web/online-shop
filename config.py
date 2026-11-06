from flask_sqlalchemy import SQLAlchemy
PORT=9595
db = SQLAlchemy()
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
DEBUG = True