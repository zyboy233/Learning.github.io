
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')

driver.find_element_by_name('username').send_keys('451253127@qq.com')

driver.find_element_by_class_name('password').send_keys('Msj_zy520520')

time.sleep(3)
username = driver.find_element_by_name('username').text
password = driver.find_element_by_class_name('password').text
print(username)
print(password)
time.sleep(3)
driver.find_element_by_name('username').clear()
driver.find_element_by_class_name('password').clear()
driver.find_element_by_xpath('//div[@class="nl_loginitem"]/input[@class="submit"]').click()