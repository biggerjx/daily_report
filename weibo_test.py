#! usr/bin/python
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json

browser = webdriver.Chrome()
browser.get("http://weibo.com/")
browser.implicitly_wait(10)
