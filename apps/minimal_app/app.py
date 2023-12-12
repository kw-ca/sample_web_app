from flask import Flask

app = Flask(__name__)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, sample web app in Flask !!!"
