from flask import Flask, redirect, request, url_for
# 加上下面這行
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

import config
from db import Database


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# 設定好剛剛的 SECRET_KEY，提醒一下，這個最好自己生成喔！
app.config['SECRET_KEY'] = b'>\x89k\xff.t{\xed\xc0\x8c^E\x81A\xe7\xb6'

# 初始化 LoginManager
login_manager = LoginManager(app)
# 如果跳到需要先登入才能看的頁面，會自動轉到叫做 login 的 function(也可以自己改)。
login_manager.login_view = "login"


# 繼承 UserMixin 類，可以不設定，可做為 ORM(物件關聯對映) 的東西(我真的不知道怎麼說)
class User(UserMixin):
    pass

# 提供使用者詳細資料，必須設定，current_user 會用到


@login_manager.user_loader
def load_user(user_id):
    user_data = Database.get(user_id)
    if user_data is None:
        return None
    user = User()
    user.username = user_data['username']
    return user


# 登入頁面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
     <form action='login' method='POST'>
     <input type='text' name='email' id='email' placeholder='email'/>
     <input type='password' name='password' id='password' placeholder='password'/>
     <input type='submit' name='submit'/>
     </form>
                  '''
    elif request.method == 'POST':
        email = request.values.get('email', None)
        password = request.values.get('password', None)

        user_data = Database.get_data(email)
        if (user_data is not None) and (password == user_data['password']):
            # 主要登入部分
            user = User()
            user.id = user_data['id']
            login_user(user)
            return redirect(url_for('home'))
        else:
            return "Account or Password are wrong"
    else:
        return 'Error'


#  登入後畫面
@app.route('/home')
@login_required  # 必須登入才能夠看到的畫面就加上這行，沒登入會自動跳轉到 login_view
def home():
    if current_user.is_active:
        return 'Welcome ' + current_user.username + '<br /><a href=' + url_for('logout') + '><button>Logout</button></a>'


# 登出畫面
@app.route('/logout')
def logout():
    logout_user()
    return 'Logged out'


if __name__ == "__main__":
    app.run()
