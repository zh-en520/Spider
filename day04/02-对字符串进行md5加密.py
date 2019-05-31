from hashlib import md5

string = '5.0'

#对字符串加密
#创建一个加密对象
s = md5()
#２．进行加密
s.update(string.encode())
#获取十六进制加密结果
result = s.hexdigest()

print(result)