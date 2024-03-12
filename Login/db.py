# 下面這坨是我懶得弄資料庫，所以假裝他是資料庫裡記錄資料就好

class Database:
    # users 是類似資料庫裡的紀錄
    users = {
        "0": {
            "email": "test01@gmail.com",
            "password": "123"
        },
        "1": {
            "email": "test02@gmail.com",
            "password": "456"
        }
    }

    user_profile = {
        "0": {
            "username": "test01"
        },
        "1": {
            "username": "test02"
        }
    }

    # 從資料庫裡抓取這個使用者
    @classmethod
    def get_data(self, email):
        for index, data in self.users.items():
            if email in data['email']:
                return {"id": index, **self.users[index]}
        return None

    # 從資料庫裡抓取這個使用者
    @classmethod
    def get(self, user_id):
        return self.user_profile[user_id]
