from fastapi import FastAPI
from routers import blog_get, blog_post, user
from database import models
from database.database import engine

start_app = FastAPI()
start_app.include_router(blog_get.router)
start_app.include_router(blog_post.router)
start_app.include_router(user.router)


@start_app.get('/')
def start_page():
    return "Hello test page"


models.Base.metadata.create_all(engine)
