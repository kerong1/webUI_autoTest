import os
import HTMLTestRunner
import unittest

from testsuites.base_testcase import Base_testcase
from Pageobjects.discuz_homepage import *
class Discuz2Search(Base_testcase):
    def test_discuz2(self):
        h=HomePagez(self.driver)
        h.Login("admin","root")
        h.sleep(5)
        s=ShanchuPage(self.driver)
        s.shanchu()
        a=AddNewModule(self.driver)
        a.addnewmodule("yyyyy")
        t=TuichuPage(self.driver)
        t.tuicu()
        t.sleep(5)
        t.tuicu()
        h.Login("root","root11")
        h.sleep(5)
        n=FatiePage(self.driver)
        n.nfatie("yyyyy","新界面","jskhfksdhgrughks")
        hf = HuitiePage(self.driver)
        hf.huifu('aaaaaaaaaa')


if __name__ == '__main__':
    unittest.main()


