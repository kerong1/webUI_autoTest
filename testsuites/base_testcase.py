from selenium import webdriver
from framework.browser_engije import BrowserEngine
import unittest
class Base_testcase(unittest.TestCase):
    def setUp(self):
        self.browser=BrowserEngine()
        self.driver=self.browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(6)


    def tearDown(self):
        self.browser.quit_browser()
        print("结束")