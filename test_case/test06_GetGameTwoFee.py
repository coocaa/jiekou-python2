# coding:utf - 8

import unittest
import requests
from common.re_token import get_token

@unittest.skip(u'无条件跳过此用例')
class GetGameTwoFee(unittest.TestCase):
    '''获取活动二设备的押金'''

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        print('获取到当前用例token值:%s' % cls.token)

        cls.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'Authorization': cls.token
        }


    def test_GetGameTwoFee(self):
        '''获取活动二设备押金'''

        self.url = 'https://www.chetanlian.com/api/services/app/GameService/GetGameTwoFee'


        r = requests.get(self.url, headers = self.headers)
        code = r.status_code
        result = r.json()
        print result
        print result['success']
        self.assertEqual(result['success'], True)



    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
