import re
import time
from urllib import request, parse
import csv
from useragent import user_agent
import random
import pymysql

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'http://maoyan.com/board/4?'
        self.page = 1
        #创建２个对象
        self.db = pymysql.connect(
            'localhost','root','123456','maoyandb',charset='utf8'
        )
        self.cursor = self.db.cursor()

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

    def write_mysql(self,html):
        ins = 'insert into top100 values(%s,%s,%s)'
        for i in html:
            L = [
                i[0].strip(),
                i[1].strip(),
                i[2].strip()[5:15]
            ]
            self.cursor.execute(ins,L)
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