from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from db import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Регистрация нового пользователя"""
    return crud.create_user(db, user)

@app.get("/beers/", response_model=list[schemas.Beer])
def read_beers(db: Session = Depends(get_db)):
    """Просмотр таблицы пива"""
    return crud.get_beers(db)

@app.get("/beers/{beer_id}", response_model=schemas.Beer)
def read_beer(beer_id: int, db: Session = Depends(get_db)):
    """Просмотр конкретного пива"""
    db_beer = crud.get_beer(db, beer_id)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """Оформление заказа"""
    return crud.create_order(db, order)
