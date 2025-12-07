
from fastapi import FastAPI, Form, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List, Annotated
import aiofiles
from pathlib import Path

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

@app.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "password": password}

class User(BaseModel):
    username: str
    password: str

@app.post('/login2')
async def login2(user: Annotated[User, Form()]):
    return user


#    文件上传 小文件 10m以下
@app.post('/upload')
async def upload_file(file: bytes = File(...)):
    with open('./data/file.jpg', 'wb') as f:
        f.write(file)
    return {'msg': 'Uploaded file'}

#    文件上传 大文件

@app.post('/upload2')
async def upload_file2(file: UploadFile):
    async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:

        # 长代码写法
        # chunk = await file.read(1024*1024)
        # while chunk:
        #     await f.write(chunk)

        # 短代码写法
        while chunk := await file.read(1024*1024):
            await f.write(chunk)

    return {'msg': 'Uploaded file'}


#    文件上传 多文件
@app.post('/betch-upload/')
async def betch_upload_file(files: List[UploadFile] = File(...)):
    for fileItem in files:
        async with aiofiles.open(f'./data/{fileItem.filename}', 'wb') as f:

            # 长代码写法
            # chunk = await file.read(1024*1024)
            # while chunk:
            #     await f.write(chunk)

            # 短代码写法
            while chunk := await fileItem.read(1024*1024):
                await f.write(chunk)
    return {'count': len(files), 'names': [f.filename for f in files]}


# 限制文件上传格式
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.gif'}

@app.post('/upload-all/')
async def upload_all(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    print('='*20, ext)
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, '不支持文件扩展名')

    async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:
        while chunk := await file.read(1024*1024):
            await f.write(chunk)
    return {'msg': 'Uploaded file'}


# 表单和文件一起上传
@app.post('/submit-form')
async def submit_form(uname: str = Form(...), file: UploadFile = File(...)):
    async with aiofiles.open(f'./data/{file.filename}', 'wb') as f:
        while chunk := await file.read(1024*1024):
            await f.write(chunk)
    return {'msg': f'{uname}已经上传{file.filename}, 上传完成'}