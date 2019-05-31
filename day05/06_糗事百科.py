from selenium import webdriver

# 创建浏览器对象
browser = webdriver.PhantomJS()
browser.get('https://www.qiushibaike.com/text/')

# 单元素查找
div=browser.find_element_by_class_name('content')

# 多元素查找
divs = browser.find_elements_by_class_name('content')
for div in divs:
    # text是获取当前节点对象中所有文本内容(所有节点)
    print(div.text)
    print('*' * 50)













