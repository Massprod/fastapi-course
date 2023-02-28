from sqlalchemy.orm.session import Session
from schemas import UserBase
from database.models import DbUser
from database.hash import Hash


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
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(id: int, db: Session, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
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
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return {"deleted": id}
