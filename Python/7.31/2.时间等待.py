# selenium 由网页驱动驱使浏览器进行操作,速度慢时一大特点
# 经常会出现代码执行完了 但是网页内容还没有加载完毕
# 里面的标签还没有显示出来 如果这时候操作里面的标签
# 就会爆出异常 NoSuchElementExpection
# 解决的办法:时间休眠 time.sleep()
# 不管页面的内容有没有加载完毕 一定要休眠指定秒数

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.find_element_by_id('kw').send_keys('hello world')

button = driver.find_element_by_id('su')
# WebDriverWait 网页等待
# 值1: 等待的对象
# 值2: 等待的时间
# WebDriverWait经常和until not 一起使用 until: 直到...
# lambda 匿名函数 is_displayed 是否已经显示
is_visible = WebDriverWait(driver , 10).until(lambda driver: button.is_displayed())
print(is_visible)
button.click()

# WebDriverWait() 和 time.sleep()
# 1.都是让程序等待指定时间
# 2.time的时间是固定的 时间长短不会随标签的加载速度而改变
    # WebDriverWait时间是不固定的 等地啊多少时间要看标签的加载时间
    # 和指定的固定的时间
# 3.如果在指定的时间内,标签仍然没有加载出来,那么二者都会爆出异常

# 隐性时间 implicility_wait