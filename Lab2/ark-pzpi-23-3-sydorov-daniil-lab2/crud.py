from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        phone=user.phone,
        email=user.email,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = get_user(db, user_id)
    if db_user:
        db_user.name = user.name
        db_user.phone = user.phone
        db_user.email = user.email
        db_user.password = user.password
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_beer(db: Session, beer_id: int):
    return db.query(models.Beer).filter(models.Beer.beer_id == beer_id).first()

def get_beers(db: Session):
    return db.query(models.Beer).all()

def create_beer(db: Session, beer: schemas.BeerCreate):
    db_beer = models.Beer(name=beer.name, type=beer.type, price=beer.price)
    db.add(db_beer)
    db.commit()
    db.refresh(db_beer)
    return db_beer

def update_beer(db: Session, beer_id: int, beer: schemas.BeerCreate):
    db_beer = get_beer(db, beer_id)
    if db_beer:
        db_beer.name = beer.name
        db_beer.type = beer.type
        db_beer.price = beer.price
        db.commit()
        db.refresh(db_beer)
    return db_beer

def delete_beer(db: Session, beer_id: int):
    db_beer = get_beer(db, beer_id)
    if db_beer:
        db.delete(db_beer)
        db.commit()
    return db_beer

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.order_id == order_id).first()

def get_orders(db: Session):
    return db.query(models.Order).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        user_id=order.user_id,
        total=order.total,
        status=order.status,
        delivery_address=order.delivery_address
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    for item in order.items:
        db_item = models.OrderItem(
            order_id=db_order.order_id,
            beer_id=item.beer_id,
            quantity=item.quantity
        )
        db.add(db_item)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
