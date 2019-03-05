from selenium.webdriver.common.by import By
from Pageobjects.base import BasePage
import time
class HomePagez(BasePage):
    home_page_username=(By.NAME,'username')
    home_page_userpwd = (By.NAME,'password')
    home_page_button=(By.CSS_SELECTOR,"button em")

    def Login(self,name,pwd):
        self.sendkeys(name,*self.home_page_username)
        self.sendkeys(pwd,*self.home_page_userpwd)
        self.click(*self.home_page_button)
        self.jihuo()
class FatiePage(BasePage):
    fatie_page_moren = (By.CSS_SELECTOR, ".fl_icn a")
    fatie_page_xinbankuai=(By.LINK_TEXT,)
    fatie_page_fatie = (By.ID, 'newspecial')
    fatie_page_title = (By.NAME, 'subject')
    iframe=(By.TAG_NAME,'iframe')
    fatie_page_neirong=(By.TAG_NAME,'body')
    fatie_page_fabiao=(By.ID,'postsubmit')

    def fatie(self,title,neirong):
        self.click(*self.fatie_page_moren)
        self.click(*self.fatie_page_fatie)
        self.sendkeys(title,*self.fatie_page_title)
        self.frame(*self.iframe)
        self.sendkeys(neirong,*self.fatie_page_neirong)
        self.jihuo()
        self.click(*self.fatie_page_fabiao)
    def nfatie(self,text,title,neirong):
        self.fatie_page_xbk = (By.LINK_TEXT, text)
        self.click(*self.fatie_page_xbk)
        self.click(*self.fatie_page_fatie)
        self.sendkeys(title,*self.fatie_page_title)
        self.frame(*self.iframe)
        self.sendkeys(neirong,*self.fatie_page_neirong)
        self.jihuo()
        self.click(*self.fatie_page_fabiao)
class HuitiePage(BasePage):
    huitie_page_button=(By.ID,'post_reply')
    huitie_page_neirong=(By.NAME,'message')
    huitie_page_fabiao=(By.ID,"postsubmit")

    def huifu(self,huifu):
        self.click(*self.huitie_page_button)
        self.jihuo()
        self.sendkeys(huifu,*self.huitie_page_neirong)
        self.click(*self.huitie_page_fabiao)
class TuichuPage(BasePage):
    tuichu_page = (By.LINK_TEXT, "退出")
    def tuicu(self):
        self.jihuo()
        self.click(*self.tuichu_page)
class ShanchuPage(BasePage):
    shanchu_page_moren = (By.CSS_SELECTOR, ".fl_icn a")
    shanchu_page_duigou=(By.NAME,"moderate[]")
    shanchu_page_shanchu=(By.LINK_TEXT,"删除")
    shanchu_page_queding=(By.ID,"modsubmit")
    def shanchu(self):
        self.click(*self.shanchu_page_moren)
        self.jihuo()
        self.click(*self.shanchu_page_duigou)
        self.click(*self.shanchu_page_shanchu)
        self.click(*self.shanchu_page_queding)
        self.jihuo()
class AddNewModule(BasePage):
    add_page_guanli=(By.LINK_TEXT,"管理中心")
    add_page_luntan=(By.LINK_TEXT,"论坛")
    add_page_iframe=(By.TAG_NAME,"iframe")
    add_page_xzmk=(By.LINK_TEXT,"添加新版块")
    add_page_xznr=(By.NAME,"newforum[1][]")
    add_page_djxz=(By.ID,"submit_editsubmit")
    def addnewmodule(self,neirong):
        self.click(*self.add_page_guanli)
        self.jihuo1(1)
        self.click(*self.add_page_luntan)
        self.frame(*self.add_page_iframe)
        self.click(*self.add_page_xzmk)
        self.clear(*self.add_page_xznr)
        self.sendkeys(neirong,*self.add_page_xznr)
        self.click(*self.add_page_djxz)
class SouSuoPage(BasePage):
    sousuo_page_title = (By.ID, 'thread_subject')
    sousuo_page_txt=(By.ID,"scbar_txt")
    sousuo_page_butten=(By.ID,'scbar_btn')
    sousuo_page_lianjie=(By.CSS_SELECTOR,'.xs3 a')
    def sousuo(self,txt):
        self.click(*self.sousuo_page_txt)
        self.sendkeys(txt,*self.sousuo_page_txt)
        # time.sleep(2)
        self.click(*self.sousuo_page_butten)
        self.jihuo1(1)
        self.click(*self.sousuo_page_lianjie)
        self.jihuo1(2)
        title=self.text(*self.sousuo_page_title)
        time.sleep(2)
        return title
class ToupiaoFatiePage(BasePage):
    tpfatie_page_moren = (By.CSS_SELECTOR, ".fl_icn a")
    tpfatie_page_fatie = (By.ID, 'newspecial')
    tpfatie_page_fqtp=(By.LINK_TEXT,'发起投票')
    tpfatie_page_title = (By.NAME, 'subject')
    tpfatie_page_neirong1=(By.XPATH,"//*[@id='pollm_c_1']/p[1]/input")
    tpfatie_page_neirong2=(By.XPATH,"//*[@id='pollm_c_1']/p[2]/input")
    fatie_page_fabiao=(By.ID,'postsubmit')

    def tpfatie(self,title,neirong1,neirong2):
        self.click(*self.tpfatie_page_moren)
        self.jihuo()
        self.click(*self.tpfatie_page_fatie)
        time.sleep(2)
        self.jihuo()
        self.click(*self.tpfatie_page_fqtp)
        self.jihuo()
        time.sleep(3)
        self.sendkeys(title,*self.tpfatie_page_title)
        self.click(*self.tpfatie_page_neirong1)
        self.sendkeys(neirong1,*self.tpfatie_page_neirong1)
        self.click(*self.tpfatie_page_neirong2)
        self.sendkeys(neirong2,*self.tpfatie_page_neirong2)
        time.sleep(3)
        self.jihuo()
        self.click(*self.fatie_page_fabiao)
        self.jihuo()
class ToupiaoPage(BasePage):
    toupiao_page_dian=(By.ID,'option_1')
    toupiao_page_button=(By.ID,"pollsubmit")
    text1=(By.CSS_SELECTOR,".pcht :first-of-type .pvt")
    t1=(By.CSS_SELECTOR,'.pcht :nth-child(2) :nth-child(2)')
    text2 = (By.XPATH, '//label[@for="option_2"]')
    t2 = (By.CSS_SELECTOR, '.pcht :nth-child(4) :nth-child(2)')
    title=(By.ID,'thread_subject')
    def toupiao(self):
        self.jihuo()
        self.click(*self.toupiao_page_dian)
        self.click(*self.toupiao_page_button)
        time.sleep(3)
        self.jihuo()
    def tx1(self):
        xuanxiang1=self.text(*self.text1)
        baifenbi1=self.text(*self.t1)
        xuanxiang2 = self.text(*self.text2)
        baifenbi2 = self.text(*self.t2)
        zhuti = self.text(*self.title)
        print("选项：", xuanxiang1, "；投票人数是：", baifenbi1)
        print("选项：", xuanxiang2, "；投票人数是：", baifenbi2)
        print("主题是：", zhuti)







