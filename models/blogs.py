from typing import List
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    comments: List[str]
    likes: int
    dislikes: int
    content: str
