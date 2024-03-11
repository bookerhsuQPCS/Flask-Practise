from flask import Flask, redirect, request, make_response, render_template, url_for


CONFIGS = {
    'ENV': 'development',
    'DEBUG': True,
    'UPLOAD_FOLDER': './file_uploads',  # 要先建好這個資料夾喔，在專案根目錄
    'ALLOW_EXTENSIONS': ['txt', 'pdf', 'png', 'jpg']
}

app = Flask(__name__)
app.config.from_mapping(CONFIGS)


@app.route('/')
def index():
    return render_template('res/index.html')


@app.route('/home', methods=['GET'])
def home():
    if 'username' in request.cookies:
        user = request.cookies.get('username')
    else:
        user = None

    return render_template('res/home.html', username=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':  # 輸入網址會進到這裡
        response = make_response(render_template('res/login.html'))
    elif request.method == 'POST':  # 表單送出後會到這裡
        account = request.values.get('username', None)
        # 驗證是否有這個使用者以及密碼是否正確，生出驗證結果 auth_result
        auth_result = 'success'  # 假設成功
        ''' 建立回應 '''
        if auth_result == 'success':  # 如果都正確
            response = make_response(redirect(url_for('home')))

            ''' 設定 Cookie '''
            response.set_cookie('username', account)
        else:  # 如果錯誤
            response = make_response(redirect(url_for('login')))
    else:
        response = make_response(redirect(url_for('index')))

    return response


@app.route('/settings', methods=['GET'])
def settings():
    if 'username' in request.cookies:
        user = request.cookies.get('username')
    else:
        user = None

    return render_template('res/settings.html', username=user)
