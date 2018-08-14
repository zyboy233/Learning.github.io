from selenium import webdriver

# 使用webkit无界面浏览器
# 如果路径为exe启动程序的路径 那么该路径需要加一个r
driver = webdriver.PhantomJS(executable_path=r'D:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# 获取指定网页的数据
driver.get('http://news.sohu.com/scroll/')

print(driver.find_element_by_class_name('title').text)