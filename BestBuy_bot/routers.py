from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from bestBuy_backend.database import get_db
from bestBuy_bot import models, schemas

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = models.User(username=user_data.username, password=user_data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_market = models.Market(name=f"{new_user.username}'s Market", user_id=new_user.id)
    db.add(new_market)
    db.commit()
    db.refresh(new_market)

    return new_user
