#encoding=utf-8
import webbrowser
from selenium import webdriver
import time
import base64
import sys
from StringIO import StringIO
from PIL import Image

class change_to_bugpage:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def search_bugs(self,url,option_one,option_two):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath("//*[@id='account']").send_keys("yanjx")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()

        self.driver.implicitly_wait(10)

        #进入'测试'模块 time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='mainmenu']/ul/li[4]").click()
        time.sleep(5)

        #进入'bug'模块
        self.driver.find_element_by_xpath("//*[@id='modulemenu']/ul/li[2]/a").click()
        #self.driver.find_element_by_xpath("//*[@id='modulemenu']/ul/li[2]/a").click()
        time.sleep(5)
        #此时界面刷新，需要重新获取元素
        #切换至财务中心
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_class_name("icon-caret-down").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("search").send_keys(u"财务中心")
        self.driver.implicitly_wait(1000)
        time.sleep(5)
        a = self.driver.find_element_by_class_name("icon-cube")
        a.click()

        #搜索
        #self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='bysearchTab']").click()

        #输入搜索条件

        self.driver.find_element_by_id("field1").find_element_by_xpath("//*[@id='field1']/option[1]").click()   #bug标题
        self.driver.find_element_by_id("operator1").find_element_by_xpath("//*[@id='operator1']/option[7]").click()  #包含
        self.driver.find_element_by_id("value1").send_keys(option_one) #标题包含啥

        self.driver.find_element_by_id("field4").find_element_by_xpath("//*[@id='field4']/option[28]").click()  #创建时间
        self.driver.find_element_by_id("operator4").find_element_by_xpath("//*[@id='operator4']/option[4]").click()   #大于等于
        self.driver.find_element_by_id("value4").send_keys(option_two)  #创建时间大于等于啥

        #提交搜索条件
        self.driver.find_element_by_xpath("//*[@id='submit']").click()

        #点击报表
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='featurebar']/div[1]/div[1]/div[2]/a").click()

        #勾选筛选条件
        time.sleep(2)
        self.driver.find_element_by_id("chartsopenedBugsPerDay").click()  #每天新增bug数
        self.driver.find_element_by_id("chartsresolvedBugsPerDay").click()  #每天解决bug数
        self.driver.find_element_by_id("chartsclosedBugsPerDay").click()   #每天关闭bug数

        #生成报告
        js = "var q=document.body.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)

        self.driver.find_element_by_id("submit").click()
        time.sleep(3)

        #对 报表进行截图
        #a = self.driver.find_element_by_tag_name('tbody')
        #a.screenshot('a.jpg')

        #self.driver.get_screenshot_as_file("test.png")


    	# 获取元素位置
    	element = self.driver.find_element_by_tag_name('tbody')
    	location = element.location
    	size = element.size
    	# 计算出元素位置图像坐标
    	img = Image.open(StringIO(base64.decodestring(self.driver.get_screenshot_as_base64())))
    	self.driver.quit()
    	left = location['x']
    	top = location['y']
    	right = location['x'] + size['width']
    	bottom = location['y'] + size['height']
    	img = img.crop((int(left), int(top), int(right), int(bottom)))

if __name__ == '__main__':

    change_to_bugpage().search_bugs("http://192.168.9.184:8080/zentao/my/","1.87.0","2017-12-08")