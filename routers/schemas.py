from pydantic import BaseModel
from datetime import datetime
from typing import List

class UserBase(BaseModel):
    userName: str
    email: str
    password: str 

class UserDisplay(BaseModel):
    userName: str
    email: str
    class Config():
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int

# display on Post
class User(BaseModel):
    userName: str
    class Config():
        orm_mode = True

class Comment(BaseModel):
    text: str
    userName: str
    timestamp: datetime
    class Config():
        orm_mode = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]
    class Config():
        orm_mode = True

class UserAuth(BaseModel):
    id: int
    userName: str
    email: str

class CommentBase(BaseModel):
    userName: str
    text: str 
    post_id: int