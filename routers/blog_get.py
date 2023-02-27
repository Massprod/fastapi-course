from fastapi import FastAPI, APIRouter, status, Response
from typing import Optional
from predefined_values import BlogType


router = APIRouter(
    prefix="/blog",
    tags=["blog"],
    )


@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates fetching all blogs",
    response_description="The list of available blogs"
    )
def order_page():
    return {"message": "all pages"}


@router.get("/type/{type}")
def type_page(type: BlogType):
    return {"message": f"Type of the blog {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def order_page(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Order of this page {id}"}


@router.get("/query/all")
def query_params(page: int = 1, page_size: Optional[int] = None):
    return {"message": f"all {page_size} blogs on page {page}"}


@router.get("/{id}/comments/{comment_id}", tags=["comments"])
def combo_query_path(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog
     - **id** mandatory path parameter
     - **comment_id** mandatory path parameter
     - **valid** optional query parameter
     - **username** optional query parameter
    """
    return {"message": f"blog_id {id} comment_id {comment_id}, valid {valid}, username {username}"}


