from extensions import db
from sqlalchemy import Column, String, Integer, PrimaryKeyConstraint, Index

class Product(db.Model):
    __tablename__ = "products"
    id = Column(Integer, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    price = Column(Integer, nullable=False)
    active = Column(Integer, nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint(id, name="pk_id"),
        Index("ix_all", name, description, price, active)
    )