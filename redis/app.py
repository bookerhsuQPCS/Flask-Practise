from flask import Flask
from flask_redis import FlaskRedis  # 增加這行

import configs


app = Flask(__name__)
app.config.from_object(configs.DevelopmentConfig)
# 剛剛的設定參數
app.config['REDIS_URL'] = "redis://localhost:6379/0"

r = FlaskRedis(app)
r.set('test', 0)


@app.route('/')
def index():
    r.incr('test')
    test = r.get('test')
    return test


if __name__ == '__main__':
    app.run()
