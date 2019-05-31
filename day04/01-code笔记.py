import requests
from lxml import etree

class NoteSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
        #web客户端验证参数，元组
        self.auth = ('tarenacode','code_2013')

    def get_pase_page(self):
        res = requests.get(
            url=self.url,
            headers=self.headers,
            auth=self.auth
        )
        res.encoding = 'utf-8'
        #xpath解析
        parse_html = etree.HTML(res.text)
        course_list = parse_html.xpath('/html/body/pre/a/text()')
        #实现输出：
        # 1.AIDCode(把/去掉)
        # 2.把../排除
        for course in course_list:
            course = course[:-1]
            if course != '..':
                print(course)


if __name__ == '__main__':
    spider = NoteSpider()
    spider.get_pase_page()