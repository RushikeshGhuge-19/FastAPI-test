import random

from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_post=[{"title": "title of post 1", "content": "content of post 1", "id":1},
         {"title": "title of post 2", "content": "content of post 2", "id":2}]

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
async def read_posts():
    return {"data": my_post}


@app.post("/posts")
def posts(post : Post):
    post_dict = post.dict()
    post_dict['id'] = random.randint(0, 1000000)
    my_post.append(post_dict)   
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    return {"post_detail": "id: {id}"}