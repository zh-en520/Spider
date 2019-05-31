'''
库：maoyandb
表：top100
插入一条表记录
'''
import pymysql

name = input('请输入电影名称：')
star = input('请输入电影主演：')
time = input('请输入上映时间：')

#创建库连接对象
db = pymysql.connect(
    'localhost','root','123456','maoyandb',charset='utf8'
)

#创建游标对象cursor
cursor = db.cursor()

#执行sql命令
ins = 'insert into top100 values(%s,%s,%s)'
cursor.execute(ins,[name,star,time])

#提交到数据库执行　commit()
db.commit()

#关闭
cursor.close()
db.close()