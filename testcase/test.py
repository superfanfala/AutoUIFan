# -*- coding: utf-8 -*-
# @Project: AutoUiFan
# @Author: rn.fan
# @File name: test
# @Create time: 2021/3/23 19:23
from selenium import webdriver
import time

driver=webdriver.Chrome('../data/chromedriver.exe')
driver.get('www.baidu.com')

time.sleep(10)
