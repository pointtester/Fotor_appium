__author__ = 'py'
# -*- coding: utf-8 -*-
from common.public.pyappium import pyappium

class page(object):
    def __init__(self,driver):
        self.driver = driver
        self.p = pyappium(self.driver)
