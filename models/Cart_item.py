from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, ForeignKeyConstraint
class CartItem(db.Model):
    __tablename__ = "cart_items"
    id = Column(Integer, autoincrement=True)
    product_id = Column(Integer, nullable=False)
    cart_id = Column(Integer, nullable=False)
    quantity = Column(Integer)
    product = db.relationship("Product", backref="cart_items")
    cart = db.relationship("Cart", backref="cart_items")
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        ForeignKeyConstraint(["product_id"], ["products.id"]),
        ForeignKeyConstraint(["cart_id"], ["carts.id"])
    )