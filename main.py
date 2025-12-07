from typing import TypeVar, Generic, Union
from fastapi import FastAPI, Request
from pydantic import BaseModel

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


@app.get('/client-info')
async def client_info(request: Request):
    return {
        'client-ip': request.client.host,
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
    }

#### 响应类型


class Item(BaseModel):
    id: int
    name: str
    tags: list[str] = []

@app.get('/item2', response_model=Item, response_model_exclude_unset=True)
async def get_item2():
    return Item(id=2, name='iphone16')


# 定义范型
T = TypeVar('T')

class SuccessResponse(BaseModel, Generic[T]):
    status: str = 'success'
    data: T


class ErrorResponse(BaseModel):
    status: str = 'error'
    message: str
    code: int = 500


@app.get('/item3/{item_id}', response_model=Union[SuccessResponse[Item], ErrorResponse])
async def get_item3(item_id: int):
    if item_id == 1:
        item = Item(id=item_id, name='iphone17', tags=['iphone', 'red'])
        # 直接实例化，不需要指定范型参数
        return SuccessResponse(data=item)
    else:
        return ErrorResponse(message="Item 没有找到", code=400)