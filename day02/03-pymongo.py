'''
库：aid1901
集合：student
文档：
'''
import pymongo

#连接对象
conn = pymongo.MongoClient('localhost',27017)

#库对象
db = conn.aid1901

#集合对象
myset = db.student

#插入语句
myset.insert_one({'姓名':'唐伯虎','年龄':23})