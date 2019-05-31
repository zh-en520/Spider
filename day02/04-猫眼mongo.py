import re
import time
from urllib import request, parse
import csv
from useragent import user_agent
import random
import pymongo

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'http://maoyan.com/board/4?'
        self.page = 1
        #创建３个对象
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['top100']

    def get_page(self,url):
        #random.choice一定要写在这里，每次请求都会随机选择
        req = request.Request(url,headers=random.choice(user_agent))
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        # print('get_page,type',type(html))
        movie_list = self.parse_page(html)
        return movie_list

    def parse_page(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)" data-act.*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</div>',re.S)
        movie_list = p.findall(html)
        print(len(movie_list))
        for i in movie_list:
            print('电影名：',i[0])
            b = i[1].strip()
            b = b.split('：')
            print('主演：',b[1])
            s = re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}',i[2])
            print('上映时间：',s)
            print('*'*10)
        return movie_list

    def write_mongo(self,html):
        for i in html:
            movie_dict = {
                '电影名称':i[0].strip(),
                '电影主演':i[1].strip(),
                '上映时间':i[2].strip()[5:15]
            }
            self.myset.insert_one(movie_dict)


    def main(self):
        for page in range(1,11):
            offset = (page-1)*10
            params = parse.urlencode({'offset':str(offset)})
            url = self.url + params
            print(url)

            html = self.get_page(url)
            print(type(html))
            # filename = '猫眼-第{}页.csv'.format(str(page))
            self.write_mongo(html)
            print(len(html))
            print('第%d页爬取成功'% self.page)
            time.sleep(0.5)
            self.page += 1



if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()