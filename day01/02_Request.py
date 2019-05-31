from urllib import request

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
#构造(包装)请求对象
req = request.Request(url,headers=headers)


#发请求，获取响应对象
res = request.urlopen(req)

#获取响应对象的内容
html = res.read().decode('utf-8')


print(html)

