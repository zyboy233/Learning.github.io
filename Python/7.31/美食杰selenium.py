from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.meishij.net/')

# 鼠标移动到菜谱大全
order = driver.find_element_by_css_selector('.hasmore a')
WebDriverWait(driver,10).until(lambda driver: order.is_displayed())
action = ActionChains(driver).move_to_element(order).perform()

# 鼠标点击孕妇标签
women = driver.find_element_by_link_text(u'孕妇')
WebDriverWait(driver,10).until(lambda driver: women.is_displayed())
women.click()

for page in range(1,3):
    print('正在查询第{}页...'.format(page))
    # 设置滚动条每次滚动四分之一
    for long in range(1,5):
        x = float(long) / 4
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' %x
        driver.execute_script(js)
        time.sleep(3)
    # 获取菜名
    titles = driver.find_elements_by_xpath('//div[@class="listtyle1"]/a')
    # titles = driver.find_elements_by_xpath('//div[@class="listtyle1"]/a/@title')
    for title in titles:
        title = title.get_attribute('title')
        print(title)
    # 下一页
    next_page = driver.find_element_by_link_text(u'下一页').click()

time.sleep(20)
driver.quit()