import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger

logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("Click back on curront page")
    def get(self,url):
        self.driver.get(url)
    def frame(self,*loc):
        el=self.find_element(*loc)
        self.driver.switch_to.frame(el)
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("%s未找到页面%s元素"%(self,loc))
    # def get_windows_img(self):
    #     file_path =os.path.dirname(os.path.abspath('.')+'/logs/')
    #     rq=time .strftime('%Y%m%d%H%M',time.localtime(time.time()))
    #     screen_name=file_path+'.png'
    #     try:
    #         self.driver.get_screenshot_as_file(screen_name)
    #         logger.info('Had take screenshot and save to folder:/screenshots')
    #     except Exception as e:
    #         self.get_windows_img()
    #         logger.error('Failed to take screenshot! %s'%e)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.send_keys(text)
        logger.info("输入内容")
    def jihuo(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def jihuo1(self,x):
        self.driver.switch_to.window(self.driver.window_handles[x])
    def click(self,*loc):
        el=self.find_element(*loc)
        el.click()
    def clear(self,*loc):
        el = self.find_element(*loc)
        el.clear()
    def sleep(self,n):
        time.sleep(n)
    def text(self,*loc):
        el = self.find_element(*loc)
        logger.info("获取内容成功")
        return el.text




