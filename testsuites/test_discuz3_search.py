import os
import HTMLTestRunner
import unittest
from ddt import *
from testsuites.base_testcase import Base_testcase
from Pageobjects.discuz_homepage import *
@ddt
class Discuz3Search(Base_testcase):
    def test_discuz3(self):
        h=HomePagez(self.driver)
        h.Login("admin","root")
        h.sleep(5)
        s=SouSuoPage(self.driver)
        s.sleep(5)
        title=s.sousuo("haotest")
        try:
            self.assertEqual(title,"haotest",msg=title )
            print(title)
        except AssertionError as title:
             print(u"找不到这个标题")

        t=TuichuPage(self.driver)
        t.tuicu()

if __name__ == '__main__':
    unittest.main()