from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
import datetime

class User(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    orders = relationship("Order", back_populates="user")

class Beer(Base):
    __tablename__ = "Beers"

    beer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    order_items = relationship("OrderItem", back_populates="beer")

class Order(Base):
    __tablename__ = "Orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String, default="Pending")
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    delivery_address = Column(String, nullable=False)

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = "OrderItems"

    order_item_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("Orders.order_id"), nullable=False)
    beer_id = Column(Integer, ForeignKey("Beers.beer_id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    beer = relationship("Beer", back_populates="order_items")
