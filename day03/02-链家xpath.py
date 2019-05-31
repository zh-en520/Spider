from urllib import request
import requests
from lxml import etree
import time

class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}'
        self.headers = {'User-Agent':'Mozilla/5.0'}


    def get_page(self,url):
        res = requests.get(url,headers=self.headers,verify=False)
        res.encoding = 'utf-8'
        html = res.text
        self.parse_page(html)


    def parse_page(self,html):
        parse_html = etree.HTML(html)
        li_list = parse_html.xpath('//*[@id="leftContent"]/ul/li[@class="clear LOGCLICKDATA"]')
        for li in li_list:
            house_name = li.xpath('./div/div[2]/div/a/text()')[0].strip()
            total_price = li.xpath('./div/div[4]/div[2]/div[1]/span/text()')[0].strip()
            unit_price = li.xpath('./div/div[4]/div[2]/div[2]/span/text()')[0].strip()

            house_dict = {
                'house_name':house_name,
                'total_price':total_price,
                'unit_price':unit_price
            }
            print(house_dict)

    def main(self):
        for i in range(1,6):
            url = self.url.format(str(i))
            self.get_page(url)
            print('第%d页爬取成功'%i)
            time.sleep(0.5)


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.main()