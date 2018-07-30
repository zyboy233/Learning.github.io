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
# 使用网页驱动来运行火狐浏览器
driver = webdriver.Firefox()
# 通过驱动来执行指定的网页
driver.get('http://www.baidu.com')
