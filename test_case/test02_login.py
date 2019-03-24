# coding:utf - 8

import unittest
import requests
from common.logger import Log


@unittest.skip(u'无条件跳过此用例')
class Blog_login(unittest.TestCase):
    '''登录接口'''
    log = Log()


    def setUp(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
        }

        self.s = requests.session()



    def test_login(self):
        '''登录'''
        self.log.info('----------start！---------')

        self.url = 'https://www.chetanlian.com/api/TokenAuth/Authenticate'

        self.data = {
            'PhoneNumber': '20000000000',
            'password': 'E10ADC3949BA59ABBE56E057F20F883E',
            'LoginType':'10'

            }

        r = self.s.post(self.url, headers = self.headers, json = self.data)
        code = r.status_code
        result = r.json()
        print result
        userId = result['result']['userId']
        print userId
        # self.log.info(u'调用登录结果: %s' % result)
        # self.log.info(u'获取是否登录成功: %s' %result[''])
        self.assertEqual(code,200)
        self.assertEqual(userId,10561)
        self.log.info('--------end!--------')


        # 获取登录后的token

        token = result['result']['accessToken']
        print token
        return token



    def tearDown(self):
        pass





if __name__ == "__main__":
    unittest.main()










