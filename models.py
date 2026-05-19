# This file handles all the models in our database.
# Helps establish schema and internal relationships.
from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

DBModelBase = declarative_base()


class Product(DBModelBase):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    base_sale_rate = Column(Integer, nullable=False)
    weekend_multiplier = Column(Float, nullable=False)

    # Relationship to sales
    sales = relationship("Sale", back_populates="product")


class Sale(DBModelBase):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sale_date = Column(Date, nullable=False)
    day_of_week = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    units_sold = Column(Integer, nullable=False)
    is_weekend = Column(Boolean, nullable=False)

    # Relationship back to product
    product = relationship("Product", back_populates="sales")
