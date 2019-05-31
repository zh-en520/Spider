import requests

class Douban(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/subject_abstract?subject_id=30414462{}'
        self.headers = {'User-Agent':'Mozilla/5.0'}

    def get_page(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        #返回的为json格式的字符串
        html = res.json()
        self.parse_page(html)

    def parse_page(self,html):
        for film_dict in html:
            name = film_dict['title'].strip()
            score = film_dict['score'].strip()
            print(name,score)

    def main(self):
        number = input('请输入电影数量：')
        url = self.url.format(number)
        self.get_page(url)

if __name__ == '__main__':
    spider = Douban()
    spider.main()