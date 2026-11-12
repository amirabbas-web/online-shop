from extensions import *
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKeyConstraint
class Payment(db.Model):
    __tablename__ = "payments"
    id = Column(Integer, autoincrement=True)
    cart_id = Column(Integer, nullable=False)
    price = Column(Integer)
    date_created = Column(String(15), default=get_corrent_time)
    token = Column(String(40))
    refid = Column(String(60))
    transaction_id = Column(String(60))
    card_pan = Column(String(60))
    status = Column(String(30), default="pending")
    cart = db.relationship("Cart", backref="payments")
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        ForeignKeyConstraint(["cart_id"], ["carts.id"])
    )