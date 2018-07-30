# selenium 硒(xi)
# selenium 是一个自动化测试工具
# 测试-----------------岗位
# 手动测试
# 自动测试
# 白盒测试:
# 黑河测试
# 在python中的应用为:
# 1.selenium可以完全模拟人对浏览器操作,对动态数据进行获取
# 动态数据由代码生成,在页面初始化的过程中是没有页无法获取
# ,但是可以通过selenium来进行获取
# 2.有些数据是进行登陆以后才能获取的,比如说:
# 好友列表,评论,消费记录...登陆以后获取cookie
# 才能进行以上操作,但是使用selenium以后,可以避免
# 人工登陆,只需账号密码即可实现selenium代替登陆

# selenium的特点:
# 1.由程序控制浏览器进行操作,而不是手动操作浏览器
# 2.程序控制浏览器进行操作的时候,速度非常慢,所以要谨慎使用selenium
# 3.使用selenium控制浏览器的时候,需要下载浏览器对应的驱动程序
# 4.selenium为开源,免费,但是更新速度没有浏览器快,不是selenium
#   更新慢,而是浏览器是更新快,注意selenium和浏览器对应关系

# 引入网页驱动
from selenium import webdriver
import time
# 使用网页驱动来运行火狐浏览器
driver = webdriver.Chrome()
# 通过驱动来执行指定的网页
driver.get('http://www.baidu.com')

# selenium提供了找到元素的方法find_element_by_XXXX
# 这些方法全部是用python实现的
# 如果只是想对这个元素进行查找 定位  建议使用xpath
# 或者css_selector
# 如果需要对找到的内容进行点击等操作
# 建议使用find_element_XXXX
# find 找到 element元素 节点 标签 by 通过

# selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="kw"]
# 错误原因:代码执行速度很快,但是浏览器响应很慢,
# 代码执行到这的时候 浏览器里面的元素可能还没有加载完
# 所以报错找不到元素

# time.sleep(3)
# 通过id查找
# driver.find_element_by_id('kw').send_keys('selenium')

# 通过name查找 属性
# driver.find_element_by_name('wd').send_keys('csdn')

# Unicode 若后面由中文 那么前面需要加一个u   r
# driver.find_element_by_class_name('s_ipt').send_keys(u'智游')

# tag_name
# driver.find_element_by_tag_name('input').send_keys('...')

# 前端 html css js
# selector 选择器
# driver.find_element_by_css_selector('#kw').send_keys('...')

# 通过xpath语法定位一个元素
# driver.find_element_by_xpath('//form[@id="form"]/span/input[@id="kw"]').send_keys('123')

#link 链接
# print(driver.find_element_by_link_text('贴吧'))

# time.sleep(5)
# driver.close()