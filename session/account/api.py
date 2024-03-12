# 新增這行
from flask import Blueprint, redirect, request, render_template, make_response, url_for


# 還有新增這行，同樣叫 app 只是我懶得改，建議還是改有意義的名字。
app = Blueprint('account', __name__)


@app.route('/home', methods=['GET'])
def home():
    if 'username' in request.cookies:
        user = request.cookies.get('username')

    return render_template('account/home.html', username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        response = make_response(render_template('account/login.html'))
    elif request.method == 'POST':  # 表單送出後會到這裡
        account = request.values.get('username', None)
        # 驗證是否有這個使用者以及密碼是否正確，生出驗證結果 auth_result
        auth_result = 'success'  # 假設成功
        ''' 建立回應 '''
        if auth_result == 'success':  # 如果都正確
            response = make_response(redirect(url_for('account.home')))

            response.set_cookie('username', account)  # 先使用 Cookie 就好
        else:  # 如果錯誤
            response = make_response(redirect(url_for('account.login')))
    else:
        response = make_response(redirect(url_for('index')))

    return response


@app.route('/settings', methods=['GET'])
def settings():
    if 'username' in request.cookies:
        user = request.cookies.get('username')

    return render_template('account/settings.html', username=user)
