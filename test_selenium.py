# coding = utf-8
from selenium import webdriver
from time import sleep, ctime

options = webdriver.ChromeOptions()

options.binary_location = "C:/Users/86130/AppData/Local/Google/Chrome/Application/chrome.exe"

chrome_driver_binary = "C:/Users/86130/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

driver.get("http://www.baidu.com")
sleep(3)
# driver.find_element_by_id("kw").send_keys("Test search")
#
#
# driver.find_element_by_id("su").click()
# sleep(3)
# driver.find_element_by_link_text('新闻').click()
# # 等待5秒
# sleep(5)
driver.find_element_by_partial_link_text('闻').click()
# 等待5秒
sleep(5)
driver.qiut()
