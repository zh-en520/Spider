import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

def get_page(url):
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    return json.loads(res.text)

def parse_page(html):
    for h in html['Data']['Posts']:
        zh_name = h['RecruitPostName']
        zh_type = h['LocationName']
        # 一级页面获取PostId,详情页URL需要此参数
        post_id = h['PostId']
        # 想办法获取到职位要求和职责,F12抓包,抓到地址
        two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1557122746678&postId=%s&language=zh-cn' % post_id
        two_html = get_page(two_url)
        # 职责
        duty = two_html['Data']['Responsibility']
        # 要求
        require = two_html['Data']['Requirement']
        print([zh_name,zh_type,duty,require])


for index in range(1,11):
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557114143837&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn' % str(index)
    html = get_page(url)
    parse_page(html)


