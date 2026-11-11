from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, Index
from flask_login import UserMixin
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(300), nullable=False)
    address = Column(String(150), nullable=False)
    phone = Column(String(11), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        Index("ix_username", username, unique=True),
        Index("ix_all", password, address, phone)
    )