from selenium import webdriver
import os

driver = webdriver.Chrome()

driver.get('file:///' + os.path.abspath('6.outframe.html'))

# frame切换
driver.switch_to.frame(driver.find_element_by_id('out'))

driver.switch_to.frame('in')

driver.find_element_by_id('kw').send_keys('selenium')

driver.find_element_by_id('su').click()