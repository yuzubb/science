import os
from flask import Flask, send_from_directory

# Vercelが自動認識できるように、オブジェクト名を「app」にします
app = Flask(__name__)

# ルート（/）にアクセスしたとき
@app.route('/')
def index():
    return '<h1>Welcome</h1><p><a href="/cns">Go to CNS page</a></p>'

# /cns にアクセスしたとき
@app.route('/cns')
def serve_cns():
    # apiフォルダの一つ上（プロジェクトのルート）にある cns.html を取得
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, '..'))
    return send_from_directory(root_dir, 'cns.html')
