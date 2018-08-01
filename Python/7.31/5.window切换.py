from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 获取当前的window对象
current_window = driver.current_window_handle
# 获取当前窗口编号和网页标题
print(current_window,driver.title)

driver.find_element_by_name('tj_trnews').click()

news = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_css_selector('.hdline0 .a3'))
news.click()

# 获取所有的窗口
all_windows = driver.window_handles
print(all_windows)

for window in all_windows:
    if window != current_window:
        # switch 切换 to 到
        driver.switch_to.window(window)
# title = driver.find_element_by_tag_name('h1')
time.sleep(2)
title = driver.find_element_by_css_selector('.text_title h1').text
# WebDriverWait(driver,10).until(lambda driver: title.is_displayed())
print(title)

time.sleep(3)
# 关闭窗口
driver.close()

driver.switch_to.window(current_window)
time.sleep(2)
print(driver.find_element_by_css_selector('#footer span').text)


# 关闭浏览器
# driver.quit()