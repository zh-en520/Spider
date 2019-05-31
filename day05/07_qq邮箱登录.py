from selenium import webdriver
import time

browser = webdriver.PhantomJS()
browser.get('https://mail.qq.com/')

# 切换到ifram子框架(网页中又嵌套了一个网页)
login_frame = browser.find_element_by_id('login_frame')
browser.switch_to_frame(login_frame)

# 输入qq号 密码 点击登录按钮
uname = browser.find_element_by_xpath('//*[@id="u"]')
uname.send_keys('2621470058')

pwd = browser.find_element_by_xpath('//*[@id="p"]')
pwd.send_keys('zhanshen001')


login = browser.find_element_by_xpath('//*[@id="login_button"]')
login.click()

time.sleep(2)
browser.save_screenshot('login.png')


