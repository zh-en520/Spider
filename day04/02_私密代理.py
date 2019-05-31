import requests

url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilla/5.0'}
proxies = {
  'http':'http://309435365:szaycclhp@42.51.205.96:16816'
}

res = requests.get(url,headers=headers,proxies=proxies)
res.encoding = 'utf-8'
print(res.text)
# '42.51.205.96:16816'
# '309435365'
# 'szayclhp'
