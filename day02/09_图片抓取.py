import requests

url = 'https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike180%2C5%2C5%2C180%2C60/sign=2d0805ddad0f4bfb98dd960662261395/a08b87d6277f9e2fa802774a1630e924b899f3b9.jpg'
headers = {
    'User-Agent':'Mozilla/5.0'
}
res = requests.get(url,headers=headers)
if res.status_code == 200:
    res.encoding = 'utf-8'
    #非结构化数据抓取，一定获取bytes数据类型
    html = res.content
    print(111)

    #保存
    with open('迪丽热巴.jpg','wb') as f:
        f.write(html)