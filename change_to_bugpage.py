#encoding=utf-8
import webbrowser
from selenium import webdriver

class change_to_bugpage:

    def __init__(self):
        self.driver = webdriver.Chrome()



    def search_bugs(self,url,option_one,option_two):
        #    driver.get(url)
        #    driver = webdriver.Chrome()

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        #    webbrowser.open(url)

        self.driver.find_element_by_xpath("//*[@id='account']").send_keys("yanjx")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()

        self.driver.implicitly_wait(10)

        #进入'测试'模块
        self.driver.find_element_by_xpath("//*[@id='mainmenu']/ul/li[4]").click()

        #进入'bug'模块
        self.driver.find_element_by_xpath("//*[@id='modulemenu']/ul/li[2]").click()

        #切换至财务中心
        self.driver.find_element_by_xpath("//*[@id='modulemenu']/ul/li[1]").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id("search").send_keys(u"财务中心")
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath("//*[@id='searchResult']/div/ul/li/a").click()
        self.driver.implicitly_wait(100)

        #搜索
        self.driver.find_element_by_xpath("//*[@id='bysearchTab']").click()

        #输入搜索条件

        self.driver.find_element_by_id("field1").find_element_by_xpath("//*[@id='field1']/option[1]").click()   #bug标题
        self.driver.find_element_by_id("operator1").find_element_by_xpath("//*[@id='operator1']/option[7]").click()  #包含
        self.driver.find_element_by_id("value1").send_keys(option_one) #标题包含啥


        self.driver.find_element_by_id("field4").find_element_by_xpath("//*[@id='field4']/option[28]").click()  #创建时间
        self.driver.find_element_by_id("operator4").find_element_by_xpath("//*[@id='operator4']/option[1]").click()   #等于
        self.driver.find_element_by_id("value4").send_keys(option_two)  #创建时间等于啥

        #提交搜索条件
        self.driver.find_element_by_xpath("//*[@id='submit']").click()


        self.driver.find_element_by_id("chartsopenedBugsPerDay").click()  #每天新增bug数
        self.driver.find_element_by_id("chartsresolvedBugsPerDay").click()  #每天解决bug数
        self.driver.find_element_by_id("chartsclosedBugsPerDay").click()   #每天关闭bug数

        #生成报告
        self.driver.find_element_by_xpath("//*[@id='submit']").click()


    # def choose_report_type(self):
    #     # 点击报表
    #     report = self.driver.find_element_by_id("featurebar").click()
    #
    #     self.driver.find_element_by_id("chartsopenedBugsPerDay").click()  #每天新增bug数
    #     self.driver.find_element_by_id("chartsresolvedBugsPerDay").click()  #每天解决bug数
    #     self.driver.find_element_by_id("chartsclosedBugsPerDay").click()   #每天关闭bug数

        #生成报告
    #    self.driver.find_element_by_xpath("//*[@id='submit']")


if __name__ == '__main__':

#    webbrowser.open("http://192.168.9.184:8080/zentao/my/","chrome")
    change_to_bugpage().search_bugs("http://192.168.9.184:8080/zentao/my/","1.87.0","2017-12-08")
#    change_to_bugpage().choose_report_type()