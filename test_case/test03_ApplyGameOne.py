# coding:utf - 8

import unittest
import requests
from common.re_token import get_token

@unittest.skip(u'无条件跳过此用例')
class ApplyGameOne(unittest.TestCase):
    '''参加活动一'''


    @ classmethod
    def setUpClass(cls):
        cls.token = get_token()
        print('获取到当前用例token值:%s' % cls.token)


        cls.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'Authorization':cls.token
        }

        cls.s = requests.session()



    def test_ApplyGameOne(self):



        '''参加活动一'''

        self.url = 'https://www.chetanlian.com/api/services/app/GameService/ApplyGameOne'

        self.data = {
                    "carNo": "辽ABCDE1"
                    }

        r = self.s.post(self.url, headers = self.headers, json = self.data)
        code = r.status_code
        result = r.json()
        print result
        self.assertEqual(code,200)
        self.assertEqual(result['success'],True)




    def tearDown(self):
        pass





if __name__ == "__main__":
    unittest.main()



