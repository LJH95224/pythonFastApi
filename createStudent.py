#
# Description: 学生表操作
# Date: 2025-12-09 15:17:16
# FilePath: \pythonFastApi\createStudent.py
#
from model19 import Student
from tortoise import Tortoise
from typing import Optional, List
import asyncio

# 1、创建学生
async def create_student(name: str, email: str, age: int = 0) -> Optional[Student]:
    """
    创建学生
    """
    try:
        stu = await Student.create(name=name, email=email, age=age)
        return stu
    except Exception as e:
        print(f"创建学生失败: {e}")
        return None

# 2、更新学生
async def update_student(stu_id: int, name: str = None, email: str = None, age: int = None) -> Optional[Student]:
    """
    更新学生
    """
    try:
        stu = await Student.get(id=stu_id)
        if not stu:
            print(f"学生 {stu_id} 不存在")
            return None
        if name:
            stu.name = name
        if email:
            stu.email = email
        if age is not None:
            stu.age = age
        await stu.save()
        return stu
    except Exception as e:
        print(f"更新学生失败: {e}")
        return None

# 3、删除学生
async def delete_student(stu_id: int) -> bool:
    """
    删除学生
    """
    try:
        stu = await Student.get(id=stu_id)
        if not stu:
            print(f"学生 {stu_id} 不存在")
            return False
        await stu.delete()
        return True
    except Exception as e:
        print(f"删除学生失败: {e}")
        return False

# 4、查询学生单条数据
async def get_student(stu_id: int) -> Optional[Student]:
    """
    查询学生单条数据
    """
    try:
        stu = await Student.get(id=stu_id)
        return stu
    except Exception as e:
        print(f"查询学生失败: {e}")
        return None

# 查询所有学生 按条件过滤，返回符合条件的学生列表
async def get_filtered_students(age: int = 18) -> Optional[List[Student]]:
    """
    查询所有学生 过滤 年龄大于指定年龄的学生
    """
    try:
        stu_list = await Student.filter(age__gt=age)
        return stu_list
    except Exception as e:
        print(f"查询所有学生失败: {e}")
        return None

# 查询，根据名称模糊搜索
async def get_name_like_students(name: str) -> Optional[List[Student]]:
    """
    查询所有学生 过滤 名称包含指定字符串的学生
    """
    try:
        stu_list = await Student.filter(name__contains=name)
        return stu_list
    except Exception as e:
        print(f"查询所有学生失败: {e}")
        return None

# 1、直接脚本测试 ------ start

# 初始化数据库
async def init():
    """
    初始化数据库 连接数据库
    """
    await Tortoise.init(
      db_url="postgres://agent:AgentPgPWD@123@117.72.214.41:5432/fastapi",
      modules={"models": ["model19"]},
    )

async def main():
    """
    主函数
    """
    await init()
    # stu1 = await create_student("张三", "zhangsan@example.com")
    # print(f"创建学生成功: {stu1.id}, {stu1.name}, {stu1.email}, {stu1.age}")
    # stu2 = await create_student("李四", "lisi@example.com", 18)
    # print(f"创建学生成功: {stu2.id}, {stu2.name}, {stu2.email}, {stu2.age}")
    # stu3 = await update_student(2, name="李四-更新", email="lisi-updated@example.com", age=20)
    # print(f"更新学生成功: {stu3.id}, {stu3.name}, {stu3.email}, {stu3.age}")
    # is_deleted = await delete_student(6)
    # print(f"删除学生成功: {is_deleted}")
    stu_list = await get_name_like_students("三")
    print(f"查询所有名称包含'三'的学生成功: {[item.name for item in stu_list]}")
    stu_list = await get_filtered_students(18)
    print(f"查询所有年龄大于18的学生成功: {[item.name for item in stu_list]}")

if __name__ == "__main__":
    # 运行主函数
    asyncio.run(main())

# 1、直接脚本测试 ------ end


