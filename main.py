
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 接口文档地址：
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs
