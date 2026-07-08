import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome</h1><p><a href="/cns">Go to CNS page</a></p>'

@app.route('/cns')
def serve_cns():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    return send_from_directory(current_dir, 'cns.html')

app = app
