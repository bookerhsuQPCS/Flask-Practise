from flask import Flask
from flask_restx import Api

from apis.api import api as account_ns
import config
from db import Database

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(config.DevelopmentConfig)


# 設定一個 API 核心(很爛，看不懂對吧，但我已經用盡我畢生的中文功力去形容了，將就一下吧)
# 第一個參數必須為 Flask 實體或是 Blueprint
# doc 為 Swagger 的路由位置
api = Api(app, version='0.0.1',
          title='Flask-RESTX and Swagger test', doc='/api/doc')


# 加入名稱空間(跟上面同樣爛)
api.add_namespace(account_ns)

# 初始化資料庫
Database.initial()
