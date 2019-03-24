# coding:utf - 8

import unittest
import requests

@unittest.skip(u'无条件跳过此用例')
class Blog_register(unittest.TestCase):
    '''注册接口'''

    def setUp(self):
        self.headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
                }
        self.s = requests.session()

    def test_register(self):
        '''注册'''

        self.url = 'https://www.chetanlian.com/api/services/app/UserService/Register'



        self.data = {
            'PhoneNumber':20000000000,
            'code':'8888',
            'password':123456
            }

        r = self.s.post(self.url, headers = self.headers, json = self.data)


        result1 = r.json()
        print result1
        result = result1['result']
        print result
        self.assertEqual(result, True)





    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()










