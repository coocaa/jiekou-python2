#conding = utf - 8

from selenium import webdriver
from common.logger import Log



driver = webdriver.Firefox()
driver.get("https://passport.jd.com/uc/login?ltype=logout")

#登录
driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[2]/a").click()
#driver.find_element_by_id("loginname").clear()
driver.find_element_by_id("loginname").send_keys("coocaaku01")
#driver.find_element_by_id("nloginpwd").clear()
driver.find_element_by_id("nloginpwd").send_keys("ku123456")
driver.find_element_by_id("loginsubmit").click()

#获得前面title,打印
title = driver.title
print title

#拿当前url与预期url做比较
if title == u'京东-欢迎登录':
    print 'title ok!'
else:
    print 'title on!'


#获取前面url,打印
now_url = driver.current_url
print now_url

#拿当前url与预期URL做比较
if now_url == 'https://www.jd.com/':
    print 'url ok!'
else:
    print 'url on!'

#获得登录成功的用户，打印
now_user = driver.find_element_by_xpath(".//*[@id='ttbar-login']/div[1]/a").text
print now_user