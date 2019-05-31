import requests

class DoubanSpider(object):
  def __init__(self):
    self.url = 'https://movie.douban.com/j/chart/' \
               'top_list?type=11&interval_id=100%3A' \
               '90&action=&start=0&limit={}'
    self.headers = {'User-Agent':'Mozilla/5.0'}

  def get_page(self,url):
    res = requests.get(url,headers=self.headers)
    res.encoding = 'utf-8'
    # 返回的为json格式的字符串
    html = res.json()
    # html: [{电影1信息},{电影2信息}]
    self.parse_page(html)

  def parse_page(self,html):
    for film_dict in html:
      # 电影名称
      name = film_dict['title'].strip()
      score = film_dict['score'].strip()
      print(name,score)

  def main(self):
    number = input('请输入电影数量:')
    url = self.url.format(number)
    self.get_page(url)

if __name__ == '__main__':
  spider = DoubanSpider()
  spider.main()








