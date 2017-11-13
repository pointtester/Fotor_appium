# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from common.public.log import Log

success = "SUCCESS"
fail = "FAIL"
logger=Log()

# 此脚本主要用于查找元素是否存在，操作页面元素
class pyappium(object):

    def __init__(self, driver=""):
        self.driver = driver

    def element_wait(self, css, secs=6):
        """
        Waiting for an element to display.

        Usage:
        driver.element_wait("id->kw",10)
        """
        if "->" not in css:
            raise NameError("定位语法错误！！, lack of '->'.")

        by = css.split("->")[0].strip()
        #strip()函数去掉前后的空格或者是其他字符
        value = css.split("->")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)), messages)
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)),messages)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def get_element(self, css):
        """
        Judge element positioning way, and returns the element.

        Usage:
        driver.get_element('id->kw')
        """
        if "->" not in css:
            raise NameError("Positioning syntax errors, lack of '->'.")

        by = css.split("->")[0].strip()
        value = css.split("->")[1].strip()

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("请输入正确的定位元素,'id','name','class','link_text','xpaht','css'.")
        return element

    def type(self, css, text):
        """
        Operation input box.

        Usage:
        driver.type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.send_keys(text)
            logger.info("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,
                css,text,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                css, text, time.time() - t1))
            raise

    def clear_type(self, css, text):
        """
        Clear and input element.

        Usage:
        driver.clear_type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.clear()
            el.send_keys(text)
            logger.info("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,
                css, text,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,
                css, text,time.time() - t1))
            raise

    def click(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id->kw")
        """
        t1 = time.time()
        try:
            self.element_wait(css)
            el = self.get_element(css)
            el.click()
            logger.info("{0} Clicked element: <{1}>, Spend {2} seconds".format(success,css,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, css, time.time() - t1))
            raise
