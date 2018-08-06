#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql
db = pymysql.connect("localhost","root","yanjiayun0629","hh" ,charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql ="""
      insert into EMPLOYEE2(name,age,sex,income) values ('yan',22,'woman',2000.0)
"""

# db.query(sql)
cursor.execute(sql)
db.commit()
# 关闭数据库连接
db.close()
