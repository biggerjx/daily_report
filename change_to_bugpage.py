#encoding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()

def search_bugs(url,option_one,option_two):
    driver.get(url)

    #进入'测试'模块
    qatopbar = driver.find_element_by_xpath("//*[@id='mainmenu']/ul/li[4]").click()

    #进入'bug'模块
    bugmodulemenu = driver.find_element_by_xpath("//*[@id='modulemenu']/ul/li[2]").click()

    #搜索
    searchbuttom  = driver.find_element_by_xpath("//*[@id='bysearchTab']").click()

    #输入搜索条件
    driver.find_element_by_id("field1").find_element_by_xpath("//*[@id='field1']/option[1]").click()   #bug标题
    driver.find_element_by_id("operator1").find_element_by_xpath("//*[@id='operator1']/option[7]").click()  #包含
    driver.find_element_by_id("// *[ @ id = 'value1_chosen'] / a").send_keys(option_one) #标题包含啥


    driver.find_element_by_id("field4").find_element_by_xpath("//*[@id='field4']/option[28]").click()  #创建时间
    driver.find_element_by_id("operator4").find_element_by_xpath("//*[@id='operator4']/option[1]").click()   #等于
    driver.find_element_by_id("//*[@id='value4']").send_keys(option_two)  #创建时间等于啥

    #提交搜索条件
    driver.find_element_by_xpath("//*[@id='submit']")


def choose_report_type():
    # 点击报表
    report = driver.find_element_by_xpath("//*[@id='featurebar']/div[1]/div[1]/div[2]/a").click()

    chartsopenedBugsPerDay = driver.find_element_by_id("chartsopenedBugsPerDay").click()  #每天新增bug数
    chartsresolvedBugsPerDay = driver.find_element_by_id("chartsresolvedBugsPerDay").click()  #每天解决bug数
    chartsclosedBugsPerDay = driver.find_element_by_id("chartsclosedBugsPerDay").click()   #每天关闭bug数

    #生成报告
    report_result = driver.find_element_by_xpath("//*[@id='submit']")





