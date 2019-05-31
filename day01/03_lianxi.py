
from urllib import request,parse


#定义常用变量
headers = {'User-Agent':'Mozilla/5.0'}
#编码并拼接url地址
key = input('请输入要搜索的内容:')
# params = parse.urlencode({'wd':key})
# url = 'http://www.baidu.com/s?'+params

#重写
params = parse.quote('迪丽热吧')
url = 'http://www.baidu.com/s?wd='+params
#构建请求对象
req = request.Request(url,headers=headers)
#获取响应对象
res = request.urlopen(req)
#提取响应内容
html = res.read().decode('utf-8')
print('type:',type(html))
filename = '%s.html' % key
with open(filename,'w',encoding='gb18030') as f:
    f.write(html)