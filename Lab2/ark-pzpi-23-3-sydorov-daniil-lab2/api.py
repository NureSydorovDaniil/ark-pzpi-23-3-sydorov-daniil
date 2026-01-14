from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from db import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/beers/", response_model=schemas.Beer)
def create_beer(beer: schemas.BeerCreate, db: Session = Depends(get_db)):
    return crud.create_beer(db, beer)

@app.get("/beers/", response_model=list[schemas.Beer])
def read_beers(db: Session = Depends(get_db)):
    return crud.get_beers(db)

@app.get("/beers/{beer_id}", response_model=schemas.Beer)
def read_beer(beer_id: int, db: Session = Depends(get_db)):
    db_beer = crud.get_beer(db, beer_id)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer

@app.put("/beers/{beer_id}", response_model=schemas.Beer)
def update_beer(beer_id: int, beer: schemas.BeerCreate, db: Session = Depends(get_db)):
    db_beer = crud.update_beer(db, beer_id, beer)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer

@app.delete("/beers/{beer_id}", response_model=schemas.Beer)
def delete_beer(beer_id: int, db: Session = Depends(get_db)):
    db_beer = crud.delete_beer(db, beer_id)
    if db_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return db_beer

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@app.get("/orders/", response_model=list[schemas.Order])
def read_orders(db: Session = Depends(get_db)):
    return crud.get_orders(db)

@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.delete("/orders/{order_id}", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.delete_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
