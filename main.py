'''
Description: ORM 对象关系映射
Date: 2025-12-08 13:21:00
FilePath: \pythonFastApi\main.py
'''
from typing import TypeVar, Generic, Union, List, Optional
from fastapi import FastAPI, Request, Query
from pydantic import BaseModel
from fastapi.responses import Response, FileResponse, StreamingResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

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

# ORM 基础配置
TORTOISE_ORM = {
    "connections": {
        # 数据库连接配置
        # 连接数据库 配置sqllite数据库 (基于文件，无需服务器)
        # "default": "sqlite://db.sqlite3"
        # postgresql 数据库连接配置
        "default": "postgres://agent:AgentPgPWD@123@117.72.214.41:5432/fastapi"
        # 连接数据库 配置mysql数据库
        # "default": "mysql://user:password@localhost:3306/dbname"
        # "default": "mysql://root:123456@localhost:3306/fastapi"
    },
    "apps": {
        "models": {
            "models": ["model19", "aerich.models"], # 模型模块和 aerich 迁移模块
            "default_connection": "default",
        },
    },
    # 连接池配置
    "use_tz": False, # 是否使用时区
    "timezone": "Asia/Shanghai", # 时区设置
    "db_pool": {
        "max_size": 10, # 连接池最大连接数
        "min_size": 1, # 连接池最小连接数
        "idle_timeout": 30, # 连接池空闲超时时间
    }
}

register_tortoise(
    # 注册 Tortoise ORM 到 FastAPI 应用
    app,
    # 配置 Tortoise ORM
    config=TORTOISE_ORM,
    # 自动生成数据库表结构
    generate_schemas=True,
    # 添加异常处理程序
    add_exception_handlers=True,
)

"""
# 数据库迁移
# 初始化数据库迁移
# aerich init -t main.TORTOISE_ORM

# 初始化数据库
# aerich init-db
# 生成数据库迁移文件
# aerich migrate --name "注释"
# 应用数据库迁移
# aerich upgrade
"""