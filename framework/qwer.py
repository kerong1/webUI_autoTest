from selenium import webdriver
import os
import time
dizhi=os.path.dirname(__file__)
zhendizhi=dizhi+"/chromedriver.exe"
dir=webdriver.Chrome(zhendizhi)
dir.implicitly_wait(5)
dir.get("http://127.0.0.1/forum.php")

dangqian=dir.current_window_handle
dir.switch_to.window(dangqian)

dir.find_element_by_name("username").send_keys("admin")      #输入用户名
dir.find_element_by_name("password").send_keys("admin")      #输入密码
dir.find_element_by_tag_name("button").click()

time.sleep(2)

dir.find_element_by_css_selector(".bm_c h2 a").click()
dir.find_element_by_id("newspecial").click()

dir.find_element_by_name("subject").send_keys("admin")
yemian=dir.find_element_by_tag_name("iframe")
dir.switch_to.frame(yemian)

dir.find_element_by_tag_name("body").send_keys("aaaaaaaaaaaaaaaaaaaaaaaaa")

dir.switch_to.window(dangqian)
dir.find_element_by_id("postsubmit").click()
time.sleep(2)
dir.find_element_by_name("message").send_keys("这是我的回复！！")
dir.find_element_by_id("fastpostsubmit").click()

dir.find_element_by_partial_link_text("退出").click()


