#-*-coding=utf-8-*

import unittest
from selenium import webdriver
from common.logger import Log

class Test(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    def test01(self):
        self.log.info('------start!----------')
        print self.driver.title
        self.log.info('-------end!----------')

    def test02(self):
        print self.driver.title


