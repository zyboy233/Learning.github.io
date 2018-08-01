# commom 共同的;公共的
# keys 键
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

time.sleep(3)
# 找到输入框 输入指定内容
driver.find_element_by_id('kw').send_keys('selenium')
time.sleep(3)
# 全选输入框内的全部内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
time.sleep(3)
driver.find_element_by_id('kw').send_keys(u'爬虫技巧')
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(5)
# 退出浏览器
driver.quit()