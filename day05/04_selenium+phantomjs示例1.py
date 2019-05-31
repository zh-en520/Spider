# 导入selenium中webdriver接口
from selenium import webdriver

# 创建phantomjs浏览器对象
driver = webdriver.PhantomJS()
# 用get方法发请求
driver.get('http://www.baidu.com/')

# print(driver.page_source.find('alkdjflkadj'))
# 查看响应内容
html = driver.page_source

# 获取截图
driver.save_screenshot('百度.png')
# 关闭浏览器
driver.quit()


















