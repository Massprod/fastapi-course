from pydantic import BaseModel
from typing import List


# Article inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str = "TestNames"
    email: str = "Testemail@gmail.com"
    password: str = "Pass12345"


class UserDisplay(BaseModel):
    username: str = "already"
    email: str = "exist"
    items: List[Article] = []

    class Config:
        orm_mode = True


# User inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User

    class Config:
        orm_mode = True
