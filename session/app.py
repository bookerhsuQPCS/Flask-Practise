from flask import Flask, redirect, request, make_response, render_template, url_for, session

# 這個 app 是 api.py 裡面的 app，建議改個有意義的名字，同樣都叫 app 是我懶得改
# 如果名稱衝突到，可以使用 as 來取個暱稱。
from account.api import app as account
from configs import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# PERMANENT_SESSION_LIFETIME：設置 session 的有效期 = Cookie 的過期時間，單位是秒。默認 Session 是永久，當 session.permanent 為 True 時才會套用。

# SESSION_COOKIE_NAME: 返回給客戶端的 Cookie 的名稱，默認是 "session"

# SESSION_COOKIE_DOMAIN: 設置 Session 的 Domain

# SESSION_COOKIE_PATH: 設置 Session 的 Path

# SERVER_NAME: 設置 Server name，不常使用

# SESSION_COOKIE_SECURE: 如果為 True，那麽只會使用 HTTPS 發送，默認為 False。

# APPLICATION_ROOT: 根路徑。

# SESSION_REFRESH_EACH_REQUEST: 是否應該為每一個請求設置cookie，默認為True，如果為False則必須顯性調用set_cookie函數；

# SESSION_COOKIE_HTTPONLY：默認為 True，表示允許 JavaScript 使用 Cookie


@app.route('/')
def index():
    return render_template('index.html')


@ app.errorhandler(404)
def page_not_found(error):
    response = make_response(render_template(
        'page_not_found.html', error=error), 404)

    return response


if __name__ == "__main__":
    app.run()
