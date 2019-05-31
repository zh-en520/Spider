import requests

url = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0'}

#向网站发起请求，并得到响应对象
res = requests.get(url,headers=headers)
#获取响应内容(字符串)
res.encoding = 'utf-8'
html = res.text

#获取bytes数据类型
print(res.content)

#获取http响应码
code = res.status_code

#获取返回数据的url地址
