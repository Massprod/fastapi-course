from fastapi import APIRouter, Depends
from schemas import ArticleBase, ArticleDisplay
from database import db_article
from database.database import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    prefix="/article",
    tags=["article"]
)


# Create Article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase,  db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# Get id article
@router.get("/{id}")
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(id, db)
