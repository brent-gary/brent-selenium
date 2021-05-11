import unittest
# coding = utf-8
from selenium import webdriver
from time import sleep, ctime

options = webdriver.ChromeOptions()

options.binary_location = "C:/Users/86130/AppData/Local/Google/Chrome/Application/chrome.exe"

chrome_driver_binary = "C:/Users/86130/AppData/Local/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)


class Log(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.baidu.com")
    def test_login(self):#登录
        driver.find_element_by_id("kw").send_keys("Test search")
    def test_dy(self):#操作1
        driver.find_element_by_id("su").click()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()