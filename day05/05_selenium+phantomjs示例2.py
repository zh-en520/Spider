from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com/')

# 向搜索框(id kw)输入 赵丽颖
ele = driver.find_element_by_xpath('//*[@id="kw"]')
ele.send_keys('赵丽颖')

time.sleep(1)
# 点击 百度一下 按钮(id su)
su = driver.find_element_by_xpath('//*[@id="su"]')
su.click()

# 截图
driver.save_screenshot('赵丽颖.png')
# 关闭浏览器
driver.quit()












