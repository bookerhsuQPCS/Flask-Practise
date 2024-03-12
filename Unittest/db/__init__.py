from redis import Redis


# 使用 Redis 假裝資料庫，並且使用 Redis 的 Hash 儲存
# name 相當於資料表，key 相當於主鍵(ID)，value 相當於其他資料(帳號、密碼)
# 我只寫了有用到的幾個 function 而已，其他要用自己加
# 實際上線的服務不要這樣玩，還有密碼不要用明文存。
class Database:
    redis_client = None

    @classmethod
    def initial(self):
        self.redis_client = Redis(host='localhost', port=6379, db=2)

    @classmethod
    def insert(self, name, key, value):
        self.redis_client.hsetnx(name, key, value)

    @classmethod
    def length(self, name):
        return self.redis_client.hlen(name)
