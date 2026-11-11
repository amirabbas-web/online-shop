from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from time import time
def get_corrent_time():
    return round(time())