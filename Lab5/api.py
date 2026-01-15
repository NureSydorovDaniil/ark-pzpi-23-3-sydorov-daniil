from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from db import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

from admin_api import router as admin_router
app.include_router(admin_router, prefix="/admin", tags=["Admin"])

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/beers/", response_model=list[schemas.Beer])
def read_beers(db: Session = Depends(get_db)):
    return crud.get_beers(db)

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders/{order_id}", response_model=schemas.Order)
def track_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
