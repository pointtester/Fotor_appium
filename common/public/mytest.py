#coding=utf-8

import unittest
from common.public.log import Log
from common.public.driver import Driver
from common.public.readconfig import ReadConfig

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### 开始！！！ ###############################')
        desired_caps=ReadConfig().read_config("../common/config/phone.conf","desired_caps","desired_caps")
        self.dr=Driver(eval(desired_caps)).driver()


    def tearDown(self):
        self.dr.quit()
        self.logger.info('###############################  结束！！！  ###############################')
