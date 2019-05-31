import re
import time

import requests
from lxml import etree
from urllib import request, parse
import csv
from useragent import user_agent
import random
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?'
        self.page = 1
        self.headers = {'User-Agent':"Mozilla/5.0"}
        # 创建２个对象
        self.db = pymysql.connect(
            'localhost', 'root', '123456', 'maoyandb', charset='utf8'
        )
        self.cursor = self.db.cursor()

    def get_page(self,url):
        res = requests.get(url,headers=self.headers,verify=False)
        res.encoding = 'utf-8'
        html = res.text
        L = self.parse_page(html)
        return L

    def parse_page(self,html):
        #创建解析对象
        parse_html = etree.HTML(html)
        dd_list = parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        #依次遍历每个节点列表，提取数据
        for dd in dd_list:
            name = dd.xpath('.//p/a/@title')[0].strip()
            star = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            time = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print([name,star,time])
            L = [name,star,time]
            return L


    def write_mysql(self,html):
        ins = 'insert into top100 values(%s,%s,%s)'
        self.cursor.execute(ins,html)
        self.db.commit()


    def main(self):
        for page in range(1,11):
            offset = (page-1)*10
            params = parse.urlencode({'offset':str(offset)})
            url = self.url + params
            print(url)

            html = self.get_page(url)
            print(type(html))
            # filename = '猫眼-第{}页.csv'.format(str(page))
            self.write_mysql(html)
            print(len(html))
            print('第%d页爬取成功'% self.page)
            time.sleep(0.5)
            self.page += 1
        self.cursor.close()
        self.db.close()



if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()