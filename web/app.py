from flask import Flask, request
from flask import render_template
from werkzeug.utils import secure_filename
from markupsafe import escape
import os


CONFIGS = {
    'ENV': 'development',
    'DEBUG': True,
    'UPLOAD_FOLDER': './file_uploads',  # 要先建好這個資料夾喔，在專案根目錄
    'ALLOW_EXTENSIONS': ['txt', 'pdf', 'png', 'jpg']
}

app = Flask(__name__)
app.config.from_mapping(CONFIGS)


# 判斷副檔名是否允許上傳
def is_allow_extensions(filename):
    return ('.' in filename) and (filename.split('.')[-1].lower() in app.config['ALLOW_EXTENSIONS'])


@app.route('/file-upload', methods=['POST'])
def file_upload():
    # 這邊 request.files['<key name>'] 的 key name 等一下會用到
    f = request.files['files']
    filename = secure_filename(f.filename)
    if is_allow_extensions(filename):
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'success'
    else:
        return 'error'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<username>')
def user_home(username):
    return render_template('index.html', username=escape(username))


@app.route('/<int:time>')
def user_list_home(time):  # 真的不知道要取什麼名字了
    users = []
    for i in range(time):
        users.append("user" + str(i))

    return render_template('res/home.html', users=users)
