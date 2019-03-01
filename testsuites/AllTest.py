from testsuites.test_discuz1_search import Discuz1Search
from testsuites.test_discuz2_search import Discuz2Search
from testsuites.test_discuz3_search import Discuz3Search
from testsuites.test_discuz4_search import Discuz4Search
import unittest
import HTMLTestRunner
import os

cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")
if not os.path.exists(report_path):os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Discuz1Search))
suite.addTest(unittest.makeSuite(Discuz2Search))
suite.addTest(unittest.makeSuite(Discuz3Search))
suite.addTest(unittest.makeSuite(Discuz4Search))



if __name__=="__main__":
    html_report=report_path+"/result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)