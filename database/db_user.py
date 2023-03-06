from sqlalchemy.orm.session import Session
from schemas import UserBase
from database.models import DbUser
from database.hash import Hash
from fastapi import HTTPException, status


def create_users(db: Session, request: UserBase):
    if db.query(DbUser).filter_by(username=request.username).first():
        return False
    else:
        new_user = DbUser(
            username=request.username,
            email=request.email,
            password=Hash().bcrypt_pass(password=request.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_one_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    return user


def update_user(id: int, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")
    new_data = DbUser(
        username=request.username,
        email=request.email,
        password=Hash().bcrypt_pass(password=request.password)
    )
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash().bcrypt_pass(password=request.password),
    })
    db.commit()
    return new_data


def delete_user(id: int, db: Session):
    if user := db.query(DbUser).filter(DbUser.id == id).first():
        db.delete(user)
        db.commit()
        return {"deleted": id}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")