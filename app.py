import random
from flask import Flask, render_template_string, request, jsonify

words = [
    "Am7", "Cmaj7", "E7", "F#dim", "ブルーススケール", "ペンタトニック",
    "チョーキング", "スライド", "プリングオフ", "スウィープ", "タッピング", "ミュート",
    "ストラトキャスター", "レスポール", "テレキャスター",
    "チューナー", "コンプレッサー", "ディストーション", "リバーブ", "ディレイ",
    "Fender", "Gibson", "PRS", "Ibanez", "Suhr", "Cort", "BOSS", "MXR", "Electro-Harmonix"
]

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>ギターフリック練習</title>
<style>
body { font-family: sans-serif; text-align: center; background: #111; color: #fff; }
#word { font-size: 2em; margin: 20px; }
input { font-size: 1.5em; padding: 10px; width: 80%; }
button { font-size: 1.2em; padding: 10px 20px; margin: 10px; }
#score { font-size: 1.5em; margin-top: 20px; }
</style>
</head>
<body>
<h1>🎸 ギター用語 フリック練習</h1>
<div id="word"></div>
<input id="input" type="text" autofocus placeholder="ここに入力">
<div>
    <button onclick="check()">送信</button>
</div>
<div id="score">スコア: 0</div>

<script>
let currentWord = "";
let score = 0;

function newWord() {
    fetch("/word").then(res => res.json()).then(data => {
        currentWord = data.word;
        document.getElementById("word").innerText = currentWord;
        document.getElementById("input").value = "";
    });
}

function check() {
    let val = document.getElementById("input").value.trim();
    if (val === currentWord) {
        score++;
        document.getElementById("score").innerText = "スコア: " + score;
    }
    newWord();
}

window.onload = newWord;
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template)

@app.route("/word")
def get_word():
    return jsonify({"word": random.choice(words)})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderが提供するPORTを使う
    app.run(host="0.0.0.0", port=port)
