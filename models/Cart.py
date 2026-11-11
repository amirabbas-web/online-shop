from extensions import db
from sqlalchemy.orm import backref
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKeyConstraint
class Cart(db.Model):
    __tablename__ = "carts"
    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    status = Column(String(30), default="pending")
    user = db.relationship("User", backref=backref("carts", lazy="dynamic"))
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        ForeignKeyConstraint(["user_id"], ["users.id"])
    )