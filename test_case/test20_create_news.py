# coding:utf - 8

import unittest
import requests
from common.re_token import get_token

@unittest.skip(u'无条件跳过此用例')
class create_news(unittest.TestCase):
    '''创建消息接口'''

    @classmethod
    def setUpClass(cls):
        cls.token = get_token()
        print('获取到当前用例token值:%s' % cls.token)

        cls.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
            'Authorization': cls.token
        }

        cls.s = requests.session()

    def test_create(self):
        '''创建消息'''

        self.url = 'https://www.chetanlian.com/api/services/app/ArticleService/Create'

        self.data = {
                    "articleSeverity": 1,
                    "createType": 0,
                    "userId": 0,
                    "theStauts": 0,
                    "title": "这个是测试的",
                    "keys": "string",
                    "description": "string",
                    "contents": "string",
                    "internalKeys": "string",
                    "lastModificationTime": "2018-08-02T06:57:45.054Z",
                    "creationTime": "2018-08-02T06:57:45.054Z",
                    "creatorUserId": 0,
                    "id": 0
                    }

        r = self.s.post(self.url, headers=self.headers, json=self.data)
        code = r.status_code
        result = r.json()
        print result

        self.assertEqual(code, 200)





    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()



