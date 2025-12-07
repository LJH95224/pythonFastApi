from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional, List
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 启动服务
# 1、通过命令 uvicorn filename:app_name --reload
# 2、通过调试 fastapi dev filename.py
# 3、通过py运行： python3 filename。
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# 接口文档地址：
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs

# 查询参数
# http://127.0.0.1:8000/query1?page=1&limit=10

@app.get('/query1')
async def page_query(page, limit):
    return {"page": page, "limit": limit}

# limit 有默认值，不是必填项
# http://127.0.0.1:8000/query1?page=1
@app.get('/query2')
async def page_limit(page: int, limit = None):
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}


# 混合
# http://127.0.0.1:8000/query3/1?limit=10
@app.get('/query3/{page}')
async def page_limit(page: int, limit = None):
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}

####### 请求参数，请求体

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

####### 请求参数，请求参数验证


# http://127.0.0.1:8000/item/12
# http://127.0.0.1:8000/item/abc 报错，item_id 定义了int
@app.get("/item/{item_id}")
async def reea_item(item_id: int):
    return {"item_id": item_id}

# http://127.0.0.1:8000/item/12
# http://127.0.0.1:8000/item/abc
# Union 变量可以被赋予多种类型
@app.get("/item3/{item_id}")
async def reea_item3(item_id: Union[int, str]):
    return {"item_id": item_id}
# Union 变量可以被赋予多种类型
# 可以使用|运算符作为Union的简洁写法，例如int | str等价于Union[int, str]
# 支持默认值
@app.get("/item4/{item_id}")
async def reea_item4(item_id: int | str = 110):
    return {"item_id": item_id}


@app.get("/item5/{item_id}")
async def reea_item5(item_id: int | None = None):
    return {"item_id": item_id}

# Optional[int] 等价于 Union[int, None]
@app.get("/item6/{item_id}")
async def reea_item6(item_id: Optional[int] = None):
    return {"item_id": item_id}


@app.get("/item7")
async def reea_item7(item_ids: List):
    return {"item_id": item_ids}

