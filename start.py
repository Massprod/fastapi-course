from fastapi import FastAPI
from routers import blog_get
from routers import blog_post


start_app = FastAPI()
start_app.include_router(blog_get.router)
start_app.include_router(blog_post.router)


@start_app.get('/')
def start_page():
    return "Hello test page"


