import requests

# 定义常用变量
post_url = 'http://www.renren.com/PLogin.do'
post_data = {
  'email' : '18633615542',
  'password' : 'zhanshen001'
}
headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
  'Referer' : 'http://www.renren.com/SysHome.do'
}
# 实例化session会话保持对象
session = requests.session()
# 先POST,把用户名和密码信息POST到一个地址
session.post(post_url,data=post_data,headers=headers)
# 再get个人主页
url = 'http://www.renren.com/969255813/profile'
res = session.get(url,headers=headers)
print(res.text)





