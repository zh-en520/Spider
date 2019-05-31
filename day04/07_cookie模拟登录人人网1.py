import requests
from lxml import etree

# url为需要登录才能正常访问的地址
url = 'http://www.renren.com/969255813/profile'
# headers中的cookie为登录成功后抓取到的cookie
headers = {
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
  "Accept-Encoding": "gzip, deflate",
  "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
  "Connection": "keep-alive",
  "Cookie": "anonymid=jwadckrc80qf4m; depovince=GW; _r01_=1; JSESSIONID=abcYgWq0uO5el_nGuWhSw; ick_login=336d3d7d-ddca-4022-a332-8935008f7fc9; first_login_flag=1; ln_uact=18633615542; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; wp_fold=0; jebe_key=a7b25d5c-2679-46f8-a359-1899ca238b46%7C2e9beece3ead42fe6a26739d515f14df%7C1559203309354%7C1%7C1559203309983; td_cookie=18446744070618257886; jebecookies=6451882c-97f5-46c5-b6a7-372da3f9c43d|||||; _de=2229A2704041535FC5E7FC3B0F076082; p=adf077cbfd215b79610c64087298159f3; t=2d63a3f1b8f80b8f230516e04f31c05b3; societyguester=2d63a3f1b8f80b8f230516e04f31c05b3; id=969255813; xnsid=f835c12b; loginfrom=syshome",
  "Host": "www.renren.com",
  "Referer": "http://www.renren.com/SysHome.do",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}

res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# 解析
parse_html = etree.HTML(res.text)
result = parse_html.xpath(
  '//*[@id="cover"]/div[2]/h1/text()'
)[0].strip()
# result:战神

print(result)











