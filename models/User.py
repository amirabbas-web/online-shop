from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, UniqueConstraint

class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True)
    username = Column(String(50), nullable=False)
    address = Column(String(150), nullable=False)
    phone = Column(String(11))
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        UniqueConstraint(username, name="uq_username")
    )