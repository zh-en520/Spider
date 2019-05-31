import urllib.request

#发请求并获取响应对象
r = urllib.request.urlopen('http://httpbin.org/get')
html = r.read().decode('utf-8')
print('type:',type(html))
# print(html)