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

    def total_price(self):
        total = 0
        for item in self.cart_items:
            t = item.price * item.quantity
            total += t
        return total

    def get_status_persion(self):
        if self.status == "pending":
            return "در انتظار پرداخت (سبد خرید)"
        if self.status == "paid":
            return "پرداخت شده"
        if self.status == "send":
            return "ارسال شده"
        if self.status == "rejected":
            return "رد شده"
        if self.status == "received":
            return "دریافت شده"