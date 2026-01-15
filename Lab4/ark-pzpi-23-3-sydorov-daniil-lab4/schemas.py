from pydantic import BaseModel
from typing import List, Optional
import datetime

class UserBase(BaseModel):
    name: str
    phone: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True

class BeerBase(BaseModel):
    name: str
    type: str
    price: float

class BeerCreate(BeerBase):
    pass

class Beer(BeerBase):
    beer_id: int

    class Config:
        orm_mode = True

class OrderItemBase(BaseModel):
    beer_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    order_item_id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    total: float
    status: Optional[str] = "Pending"
    order_date: Optional[datetime.datetime] = None
    delivery_address: str

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class Order(OrderBase):
    order_id: int
    items: List[OrderItem] = []

    class Config:
        orm_mode = True
