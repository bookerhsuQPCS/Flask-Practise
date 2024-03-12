from flask import Flask
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension

import config


# templates 的位置記的修改一下
app = Flask(__name__, template_folder='../templates')
# 設定檔裡面不要忘記要設定有關 Email 的各種設定
app.config.from_object(config.DevelopmentConfig)

mail_app = Mail(app)

toolbar = DebugToolbarExtension(app)
