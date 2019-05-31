import requests

url = 'http://tieba.baidu.com/f?'
params = {
    'kw':'校花吧',
    'pn':'50'
}
headers = {'User-Agent':'Mozilia/5.0'}
#自动对params进行编码，然后自动和url进行拼接
res = requests.get(url,params=params,headers=headers)
res.encoding = 'utf-8'
print(res.text)