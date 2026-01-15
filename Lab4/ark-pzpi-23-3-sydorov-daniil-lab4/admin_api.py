from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import schemas
from db import get_db

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    crud.delete_user(db, user_id)
    return {"message": "Користувача видалено"}

@router.post("/beers")
def add_beer(name: str, type: str, price: float, db: Session = Depends(get_db)):
    beer_data = schemas.BeerCreate(name=name, type=type, price=price)
    return crud.create_beer(db, beer_data)


@router.delete("/beers/{beer_id}")
def delete_beer(beer_id: int, db: Session = Depends(get_db)):
    beer = crud.get_beer(db, beer_id)
    if not beer:
        raise HTTPException(status_code=404, detail="Пиво не знайдено")

    crud.delete_beer(db, beer_id)
    return {"message": "Пиво видалено"}

@router.get("/orders")
def get_all_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)


@router.put("/orders/{order_id}/status")
def change_order_status(order_id: int, status: str, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Замовлення не знайдено")

    order.status = status
    db.commit()
    db.refresh(order)
    return order


@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = crud.get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Замовлення не знайдено")

    crud.delete_order(db, order_id)
    return {"message": "Замовлення видалено"}
