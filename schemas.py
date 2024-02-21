from typing import List
from pydantic import BaseModel

#class usercreate(basemodel):

class User(BaseModel):
    id: int
    username: str
    email: str


class CommentCreate(BaseModel):
    comment: str
    owner_id: int
    content_id: int

class Comment(CommentCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  
        #Pydantic'in bu modelin bir ORM (Object-Relational Mapping) modeli olduğunu ve SQLAlchemy modelleriyle uyumlu olduğunu belirtir.


class ContentBase(BaseModel):
    title: str
    description: str

class ContentCreate(ContentBase):
    title: str
    description: str
    comment_id: int
    review_point: int


class Content(ContentBase):
    id: int
    comments: List[Comment] = []

    class Config:
        orm_mode = True





