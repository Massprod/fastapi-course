from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from database import db_article
from schemas import UserBase
from database.database import get_db
from sqlalchemy.orm import Session
from authentication.oauth2 import get_current_user


router = APIRouter(
    prefix="/article",
    tags=["article"]
)


# Create Article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase,
                   db: Session = Depends(get_db),
                   current_user: UserBase = Depends(get_current_user)
                   ):
    return db_article.create_article(db, request)


# Get id article
@router.get("/{id}")
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {"data": db_article.get_article(id, db),
            "current_user": current_user
            }
