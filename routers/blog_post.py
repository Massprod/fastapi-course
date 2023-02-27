from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    number_comments: int
    published: Optional[bool]
    tags: List[str] = ["tag1", "tag2"]
    metadata: Dict[str, str] = {"key1": "value1"}
    image: Optional[Image] = None


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        "id": id,
        "data": blog,
        "version": version,
    }


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(blog: BlogModel, id: int,
                   comment_title: str = Query(None,
                                              title="Title of the comment",
                                              description="Some description for comment Title",
                                              alias="commentTitle",
                                              deprecated=True,
                                              ),
                   content: str = Body(...,  # or Ellipsis == ... making this parameter required
                                       min_length=10,
                                       max_length=50,
                                       alias="commentContent",
                                       regex="^[a-z/s]*$",
                                       ),
                   v: Optional[List[str]] = Query(["1.0", "1.1", "1.2"],
                                                  description="Version of comment",
                                                  alias="Version",
                                                  min_length=2,  # validate len(list) and len(str)
                                                  ),
                   comment_id: int = Path(None, gt=5, le=10)  # gt - greater than, ge - greater and equal, same lower
                   ):
    return {
        "id": id,
        "blog": blog,
        "comment_id": comment_id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
    }
