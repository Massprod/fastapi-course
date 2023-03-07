from fastapi import FastAPI, Request, HTTPException, status
from routers import blog_get, blog_post, user, article, product, file
from database import models
from database.database import engine
from exceptions import StoryException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from authentication import authentication_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication_router.router)
app.include_router(file.router)


@app.get('/')
def start_page():
    return "Hello test page"


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exception: StoryException):
    return JSONResponse(status_code=418,
                        content={"detail": exception.name})


# @start_app.exception_handler(HTTPException)
# def custom_handler(request: Request, exception: StoryException):
#     return PlainTextResponse(str(exception), status_code=status.HTTP_400_BAD_REQUEST)


models.Base.metadata.create_all(engine)

# for CORS error (multiple services on 1 local machine)
origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/files", StaticFiles(directory="files"), name="files")
