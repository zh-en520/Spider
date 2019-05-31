from urllib import request, parse

class TiebaSpider(object):
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0'}
    #获取页面（响应内容)
    def get_page(self,url):
        req = request.Request(url,headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html
    #解析页面(提取数据)
    def parse_page(self):
        pass
    #保存数据
    def write_page(self,filename,html):
        with open(filename,'w') as f:
            f.write(html)
    #主函数
    def main(self):
        name = input('请输入贴吧名')
        startpage = int(input('请输入起始页'))
        endpage = int(input('请输入终止页'))
        for page in range(startpage,endpage+1):
            pn = (page-1)*50
            params = parse.urlencode({'kw':name,'pn':str(pn)})
            url = 'http://tieba.baidu.com/f?'+params

            #发送请求获取页面
            html = self.get_page(url)
            filename = '{}-第{}页.html'.format(name,str(page))
            self.write_page(filename,html)
            print('第%d页爬取成功'%page)

if __name__ == '__main__':
    spider = TiebaSpider()
    spider.main()