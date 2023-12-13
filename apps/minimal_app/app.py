import logging
import os

from email_validator import EmailNotValidError, validate_email
from flask import (
    Flask,
    flash,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message


def check_form_values(username, email, desc):
    is_valid = True
    if not username:
        flash("ユーザー名は必須です")
        is_valid = False
    if not email:
        flash("メールアドレスは必須です")
        is_valid = False
    try:
        validate_email(email)
    except EmailNotValidError:
        flash("メールアドレスの形式で入力してください")
        is_valid = False
    if not desc:
        flash("問い合わせ内容は必須です")
        is_valid = False
    return is_valid


def send_email(mail, to, subject, template, **kwargs):
    """メールを送信する関数"""
    pass
    # msg = Message(subject, recipients=[to])
    # msg.body = render_template(template + ".txt", **kwargs)
    # msg.html = render_template(template + ".html", **kwargs)
    # mail.send(msg)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "X2fbZ3h0BAk7bRXhG2CHEfW6ISBVsdz1"
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    toolbar = DebugToolbarExtension(app)
    app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
    app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
    app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
    app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")
    mail = Mail(app)
    app.logger.setLevel(logging.DEBUG)

    # URLと実行する関数をマッピングする
    @app.route("/")
    def index():
        return "Hello, sample web app in Flask !!!"

    @app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
    def hello(name):
        return f"Hello, {name}!!!!"

    @app.route("/show_name/<name>")
    def show_name(name):
        return render_template("index.html", name=name)

    @app.route("/contact")
    def contact():
        # レスポンスオブジェクトを取得する
        response = make_response(render_template("contact.html"))
        # クッキーを設定する
        response.set_cookie("sample_web_app_key", "sample_web_app_value")
        # セッションを設定する
        session["username"] = "ichiro"
        # レスポンスオブジェクトを返す
        return response

    @app.route("/contact/complete", methods=["GET", "POST"])
    def contact_complete():
        if request.method == "POST":
            # form属性を使ってフォームの値を取得する
            username = request.form["username"]
            email = request.form["email"]
            desc = request.form["description"]

            if not check_form_values(username, email, desc):
                print("not valid!!!")
                return redirect(url_for("contact"))
            # メールを送る
            send_email(
                mail,
                email,
                "問い合わせありがとうございました。",
                "contact_email",
                username=username,
                desc=desc,
            )

            # contactエンドポイントへリダイレクトする
            return redirect(url_for("contact_complete"))

        return render_template("contact_complete.html", username="username")

    with app.test_request_context():
        # /
        print(url_for("index"))

        # /hello/world
        print(url_for("hello-endpoint", name="world"))

        # /show_name/ichiro?page=1
        print(url_for("show_name", name="ichiro", page="1"))

    return app
