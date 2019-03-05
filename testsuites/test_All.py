
import unittest
import HTMLTestRunner
import os
import sys
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
#
# cur_path=os.path.dirname(os.path.realpath(__file__))
# report_path=os.path.join(cur_path,"report")

# if not os.path.exists(rootPath):os.mkdir(rootPath)

sys.path.append("E:\\Dis\\")
dir='./'
# c_path=os.path.dirname(os.path.realpath(__file__))
c_path=os.path.dirname(os.path.abspath('.'))
report_path=os.path.join(c_path,'report')
if not os.path.exists(report_path): os.mkdir(report_path)
suite=unittest.TestLoader().discover(dir,pattern='test_discuz*')
#
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Discuz1Search))
# suite.addTest(unittest.makeSuite(Discuz2Search))
# suite.addTest(unittest.makeSuite(Discuz3Search))
# suite.addTest(unittest.makeSuite(Discuz4Search))
if __name__=="__main__":
    html_report=report_path+r'\result.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)