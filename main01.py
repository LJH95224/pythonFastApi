import uvicorn
from fastapi import FastAPI

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
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# 接口文档地址：
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redocs