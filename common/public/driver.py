#coding=utf-8
from selenium import webdriver
from common.public.log import Log
from common.public.readconfig import ReadConfig

logger=Log()

class Driver:

    def __init__(self,desired_caps):
        self.desired_caps=desired_caps

    def driver(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return driver

#test coding
#t=Browser("../../config/config.conf")
#print(t)
#t.driver()