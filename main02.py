from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
# 接口文档地址：
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# http://127.0.0.1:8000/user
# {user: 'dd', age:17}
@app.post('/user')
async def create_user(user: dict):
    return user


class User(BaseModel):
    name: str
    age: int
    sex: str = "男"


@app.post('/user2')
async def create_user(user: User):
    return user



