__author__ = 'py'

import configparser

class ReadConfig:

    def read_config(self,path,section,option):
        cf=configparser.ConfigParser()
        cf.read(path)
        return cf[section][option]

# test coding
# t=ReadConfig().read_config("../config/phone.conf","desired_caps","desired_caps")
# t=eval(t)
# print(type(t))
