from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('http://www.taobao.com')

driver.find_element_by_id('q').send_keys(u'笔记本电脑')
driver.find_element_by_class_name('btn-search').click()

for page in range(1,3):
    print('正在爬取第{}页数据'.format(page))
    # 1,3,5,7,9,11
    for row in range(1,13,2):
        x = float(row) / 10
        # document 网页
        # documentElement 网页标签
        # scroll 滑动
        # scrollTop 从屏幕顶部往下滑动多少
        # 计算每次移动的代码片段 在python里面不能执行js代码 所以将代码写成字符串形式
        # scrollHeight 整个网页内可以滑动的长度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % x
        driver.execute_script(js)
        time.sleep(3)

    item_list = driver.find_elements_by_class_name('grid-item')
    for item in item_list:
        with open('computer.txt','a',encoding='utf-8')as f:
            f.write(item.text)
            f.write('\n')
    driver.find_element_by_class_name('J_Ajax').click()