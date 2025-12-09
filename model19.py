'''
Description: 用户模型
Date: 2025-12-08 17:46:37
FilePath: \pythonFastApi\model19.py
'''
from tortoise.models import Model
from tortoise.fields import CharField, DatetimeField, BooleanField, IntField

class User(Model):
    id = CharField(max_length=36, pk=True)  # 主键，UUID 字符串
    name = CharField(max_length=64, unique=True)  # 用户名，唯一
    email = CharField(max_length=255, unique=True)  # 邮箱，唯一
    is_active = BooleanField(default=True)  # 是否激活
    age = IntField(default=0)  # 年龄，默认值为 0
    created_at = DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = DatetimeField(auto_now=True)  # 更新时间

    class Meta:
        table = "users"  # 自定义表名
        unique_together = ("name", "email")  # 联合唯一约束
        ordering = ["-created_at"]  # 默认按创建时间降序排序 - 表示降序 + 表示升序

    def __str__(self):
        return self.name

class Student(Model):
    """
    学生模型
    """
    id = IntField(pk=True, description="学生ID, 主键")  # 主键，自增整数
    name = CharField(max_length=64, unique=True, description="学生姓名, 唯一")  # 用户名，唯一
    email = CharField(max_length=255, unique=True, null=True, description="学生邮箱, 唯一")  # 邮箱，唯一
    age = IntField(default=0)  # 年龄，默认值为 0
    created_at = DatetimeField(auto_now_add=True)  # 创建时间
    updated_at = DatetimeField(auto_now=True)  # 更新时间

    class Meta:
        table = "students"  # 自定义表名
        unique_together = ("name", "email")  # 联合唯一约束
        ordering = ["-created_at"]  # 默认按创建时间降序排序 - 表示降序 + 表示升序

    def __str__(self):
        return f"学生ID: {self.id}, 姓名: {self.name}, 邮箱: {self.email}, 年龄: {self.age}"
