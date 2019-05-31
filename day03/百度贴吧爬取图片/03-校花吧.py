import requests
from lxml import etree
from urllib import parse
import datetime, random

class BaiduTieba(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}

    def get_page(self,params):
        res = requests.get(self.url,params=params,headers=self.headers,verify=False)
        res.encoding = 'utf-8'
        html = res.text
        return html


    def parse_one_page(self,html,params):
        parse_html = etree.HTML(html)
        all_list = parse_html.xpath('//*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a[@class="j_th_tit "]/@href')
        for url_title in all_list:
            url = 'http://tieba.baidu.com' + url_title
            html = self.get_page(params)
            img_list = self.parse_two_page(html)
            for img in img_list:
                res = requests.get(img, headers=self.headers)
                res.encoding = 'utf-8'
                img_html = res.content
                filename = img[-10:]
                self.write(filename,img_html)


    def parse_two_page(self,html):
        parse_html = etree.HTML(html)
        img_list = parse_html.xpath('//*[@class="d_post_content j_d_post_content  clearfix"]/img/@src')
        return img_list

    def write(self,filename,img_html):
        with open(filename,'wb') as f:
            f.write(img_html)
            print(filename,'下载成功')



    def main(self):
        name = input('请输入要爬取的贴吧名：')
        start = int(input('请输入要爬取的起始页'))
        end = int(input('请输入要爬取的终止页'))
        for i in range(start,end+1):
            pn = (i-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            html = self.get_page(params)
            self.parse_one_page(html,params)



if __name__ == '__main__':
    spider = BaiduTieba()
    spider.main()

