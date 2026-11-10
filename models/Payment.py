from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKeyConstraint
class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, autoincrement=True)
    cart_id = Column(Integer, nullable=False)
    status = Column(String(30), default="pending")
    cart = db.relationship("Cart", backref="payments")
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        ForeignKeyConstraint(["cart_id"], ["carts.id"])
    )