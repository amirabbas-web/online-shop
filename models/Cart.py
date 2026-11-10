from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKeyConstraint
class Cart(db.Model):
    __tablename__ = "carts"
    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    status = Column(String(30), default="pending")
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        ForeignKeyConstraint(["user_id"], ["users.id"])
    )