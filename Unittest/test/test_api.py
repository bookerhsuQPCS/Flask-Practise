import json

from . import BaseTestCase


class TestAccountApi(BaseTestCase):
    def test_register(self):
        # 實際送出請求
        response = self.client.post(
            '/account/register',
            data=json.dumps({
                'email': 'test01@gmail.com',
                'password': 'test'
            }),
            content_type='application/json'
        )

        # 判斷回應是否正確
        self.assertEqual(response.json, {'status': '0', 'message': ''})
        self.assertEqual(response.status_code, 200)
