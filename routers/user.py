from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_user
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# Create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_users(db, request)


# Read all user
@router.get("/all", response_model=List[UserDisplay])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user
@router.get("/{id}", response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_one_user(db, id)


# Update user
@router.post("/{id}", response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(id, db, request)


# Delete user
@router.post("/delete/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(id, db)
