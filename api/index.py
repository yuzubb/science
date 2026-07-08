import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# ルート（/）にアクセスしたとき（ダーク・ライト・端末同期対応）
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Science Home</title>
        <style>
            /* デフォルト（ライトモード）の変数を定義 */
            :root {
                --bg-color: #ffffff;
                --text-color: #333333;
                --link-color: #0066cc;
                --card-bg: #f5f5f7;
            }

            /* 端末の設定がダークモードの時の自動切り替え */
            @media (prefers-color-scheme: dark) {
                :root {
                    --bg-color: #1c1c1e;
                    --text-color: #f5f5f7;
                    --link-color: #64d2ff;
                    --card-bg: #2c2c2e;
                }
            }

            /* 手動切り替え用のクラス（JavaScriptで制御） */
            body.light-theme {
                --bg-color: #ffffff;
                --text-color: #333333;
                --link-color: #0066cc;
                --card-bg: #f5f5f7;
            }
            body.dark-theme {
                --bg-color: #1c1c1e;
                --text-color: #f5f5f7;
                --link-color: #64d2ff;
                --card-bg: #2c2c2e;
            }

            /* スタイリング */
            body {
                background-color: var(--bg-color);
                color: var(--text-color);
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                transition: background-color 0.3s, color 0.3s;
            }

            .container {
                text-align: center;
                padding: 2rem;
                background-color: var(--card-bg);
                border-radius: 16px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.05);
                transition: background-color 0.3s;
            }

            h1 {
                margin-bottom: 0.5rem;
            }

            a {
                color: var(--link-color);
                text-decoration: none;
                font-weight: bold;
                font-size: 1.1rem;
            }

            a:hover {
                text-decoration: underline;
            }

            /* モード切り替えボタンのエリア */
            .btn-group {
                margin-top: 1.5rem;
                display: flex;
                gap: 8px;
                justify-content: center;
            }

            button {
                padding: 6px 12px;
                border: none;
                border-radius: 20px;
                background-color: var(--text-color);
                color: var(--bg-color);
                cursor: pointer;
                font-size: 0.85rem;
                font-weight: 500;
                transition: opacity 0.2s;
            }

            button:hover {
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Science</h1>
            <p><a href="/cns">Go to CNS page →</a></p>
            
            <div class="btn-group">
                <button onclick="setTheme('light')">☀️ Light</button>
                <button onclick="setTheme('dark')">🌙 Dark</button>
                <button onclick="setTheme('auto')">💻 Auto (端末設定)</button>
            </div>
        </div>

        <script>
            // テーマを切り替えるJavaScript
            function setTheme(mode) {
                const body = document.body;
                if (mode === 'light') {
                    body.classList.add('light-theme');
                    body.classList.remove('dark-theme');
                    localStorage.setItem('theme', 'light');
                } else if (mode === 'dark') {
                    body.classList.add('dark-theme');
                    body.classList.remove('light-theme');
                    localStorage.setItem('theme', 'dark');
                } else {
                    // 自動モード（クラスを消してCSSの@mediaに任せる）
                    body.classList.remove('light-theme', 'dark-theme');
                    localStorage.removeItem('theme');
                }
            }

            // ページを開いたときに保存された設定があれば再現する
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme) {
                setTheme(savedTheme);
            }
        </script>
    </body>
    </html>
    """

# /cns にアクセスしたとき
@app.route('/cns')
def serve_cns():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, '..'))
    return send_from_directory(root_dir, 'cns.html')
