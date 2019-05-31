from urllib import request
import re

class FilmSpider(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net'
        self.headers = {'User-Agent':'Mozilla/5.0'}

    #定义功能，不要把url写死了
    def get_page(self,url):
        req = request.Request(
            url = url,
            headers=self.headers
        )

        res = request.urlopen(req)

        html = res.read().decode('gb18030')
        return html

    #解析一级页面
    def parse_one_page(self,html):
        p = re.compile('<table width="100%".*?<a href="(.*?)" class="ulink">(.*?)</a>.*?</table>',re.S)
        film_list = p.findall(html)
        for film in film_list:
            film_name = film[1].strip()
            film_link = self.url + film[0].strip()
            down_link = self.get_download_link(film_link)
            print(film_name,down_link)

    def get_download_link(self,film_link):
        html = self.get_page(film_link)
        p = re.compile('<tbody>.*?href="(.*?)">.*?</a>',re.S)
        link_list = p.findall(html)
        return link_list[0]


if __name__ == '__main__':
    spider = FilmSpider()
    html = spider.get_page('https://www.dytt8.net/html/gndy/dyzz/index.html')
    spider.parse_one_page(html)