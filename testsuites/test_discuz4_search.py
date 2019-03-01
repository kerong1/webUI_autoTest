import os
import HTMLTestRunner
import unittest

from testsuites.base_testcase import Base_testcase
from Pageobjects.discuz_homepage import *
class Discuz4Search(Base_testcase):
    def test_discuz4(self):
        h=HomePagez(self.driver)
        h.Login("admin","root")
        h.sleep(5)
        t=ToupiaoFatiePage(self.driver)
        t.tpfatie("发起投票","选项1","选项2")
        time.sleep(5)
        tt=ToupiaoPage(self.driver)
        tt.toupiao()
        tt.tx1()
        time.sleep(5)


    if __name__ == '__main__':
        unittest.main()

