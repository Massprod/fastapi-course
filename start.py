from fastapi import FastAPI, Request, HTTPException, status
from routers import blog_get, blog_post, user, article, product
from database import models
from database.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware


start_app = FastAPI()
start_app.include_router(blog_get.router)
start_app.include_router(blog_post.router)
start_app.include_router(user.router)
start_app.include_router(article.router)
start_app.include_router(product.router)


@start_app.get('/')
def start_page():
    return "Hello test page"


@start_app.exception_handler(StoryException)
def story_exception_handler(request: Request, exception: StoryException):
    return JSONResponse(status_code=418,
                        content={"detail": exception.name})


# @start_app.exception_handler(HTTPException)
# def custom_handler(request: Request, exception: StoryException):
#     return PlainTextResponse(str(exception), status_code=status.HTTP_400_BAD_REQUEST)


models.Base.metadata.create_all(engine)


origins = [
    "http://localhost:8000"
]

start_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

