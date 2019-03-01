import os
import HTMLTestRunner
import unittest
from testsuites.base_testcase import Base_testcase
from framework.browser_engije import BrowserEngine
from Pageobjects.discuz_homepage import *

class Discuz1Search(Base_testcase):
    def test_discuz1(self):
        h=HomePagez(self.driver)
        # h.get("http://127.0.0.1/forum.php")
        h.Login("admin","root")
        h.sleep(5)
        f=FatiePage(self.driver)
        f.fatie("title","绝对是工行入")
        f.sleep(5)
        hf=HuitiePage(self.driver)
        hf.huifu('aaaaaaaaaa')
        hf.sleep(5)
        t = TuichuPage(self.driver)
        t.tuicu()
if __name__=='__main__':
    unittest.main()