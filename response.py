'''
Description: 响应类型
Autor: Alfred
Date: 2025-12-08 13:21:00
FilePath: \pythonFastApi\response.py
'''
from typing import TypeVar, Generic, Union, List, Optional
from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from fastapi.responses import Response, FileResponse, StreamingResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

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

#### 响应类型 JSON数据


class Item(BaseModel):
    id: int
    name: str
    category: str
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
        item = Item(id=item_id, name='iphone17', category='iphone', tags=['iphone', 'red'])
        # 直接实例化，不需要指定范型参数
        return SuccessResponse(data=item)
    else:
        return ErrorResponse(message="Item 没有找到", code=400)

# 响应数据 - 列表数据


DB = [Item(id=i, name=f'iphone{i}', category='iphone' if i%2 == 0 else 'ipad', tags=['iphone', 'red', 'green']) for i in range(1, 101)]

@app.get('/item4/list')
async def get_item4_list():
    items = DB[:10]
    return SuccessResponse(data=items)


@app.get('/item5', response_model=Union[SuccessResponse[List[Item]], ErrorResponse])
async def get_item5(category: Optional[str] = Query(None, description="分类")):
    temp = []
    # 复杂代码
    # if category:
    #    for item in DB:
    #        if item.category == category:
    #            temp.append(item)

    # 简单代码
    if category:
        temp = [item for item in DB if item.category == category]
    else:
        temp = DB
    return SuccessResponse(data=temp)


class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    data: List[Item] = []

@app.get('/item6', response_model=Union[SuccessResponse[Pagination], ErrorResponse])
async def get_item6(
    category: Optional[str] = Query(None, description="分类"),
    page: int = Query(1, ge=1, description="页码"), 
    page_size: int = Query(10, ge=1, le=100, description="每页数量")):
    temp = []
    # 复杂代码
    # if category:
    #    for item in DB:
    #        if item.category == category:
    #            temp.append(item)

    # 简单代码
    if category:
        temp = [item for item in DB if item.category == category]
    else:
        temp = DB

    # 分页
    start = (page - 1) * page_size
    end = start + page_size
    temp = temp[start:end]
    total = len(temp)
    pagination = Pagination(page=page, page_size=page_size, total=total, data=temp)

    return SuccessResponse(data=pagination)


# 响应数据-文本格式
@app.get('/download-fileText')
async def get_custom_file():
    info = b"File Content"
    return Response(
        content=info,
        # 响应体的媒体类型 文本类型
        media_type="text/plain",
        # 响应头 附件类型 文件名 attachment -> 浏览器会下载文件 filename=file.txt 下载文件名
        headers={"Content-Disposition": "attachment; filename=file.txt"})


@app.get('/download-filePdf')
async def get_custom_file2():
    info = b"File Content"
    path = './data/FastAPI文档.pdf'
    return FileResponse(path, media_type='application/pdf', filename='FastAPI文档.pdf')


# FileResponse 响应文件 适合小文件下载，如果文件太大，不建议使用 FileResponse
# 因为 FileResponse 会将文件内容读取到内存中，然后返回给客户端
# 如果文件太大，会导致内存占用过高，甚至导致内存溢出
# 建议使用 StreamingResponse 来响应文件，StreamingResponse 会将文件内容分块返回给客户端
# 客户端可以边接收边处理文件，而不需要等待整个文件下载完成

# 定义一个生成器函数，用于分块读取文件内容
# chunk_size 分块大小 10MB
# 每次读取 10MB 数据，返回给客户端

def generate_chunk(file_path: str, chunk_size: int = 1024 * 1024 * 10):
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            yield chunk

@app.get('/download-video')
async def get_custom_file3():
    path = './data/vide1.mp4'
    return StreamingResponse(
        content=generate_chunk(path),
        media_type='video/mp4',
        # 响应头 附件类型 文件名 attachment -> 浏览器会下载文件 filename=vide1.mp4 下载文件名
        headers={"Content-Disposition": "attachment; filename=vide1.mp4"})

# 响应数据 -  其他数据类型

@app.get('/string1')
async def get_string1():
    return Response(content="Hello World", media_type="text/plain")

@app.get('/string2', response_class=HTMLResponse)
async def get_string2():
    return "<html><body><h1 style='color:red'>Hello World</h1></body></html>"


@app.get('/redirect')
async def get_redirect():
    return RedirectResponse(url="/string2")

# 挂载静态文件目录
# 访问 http://127.0.0.1:8000/static/index.html 即可访问 template 目录下的 index.html 文件

app.mount("/static", StaticFiles(directory="template"), name="static")