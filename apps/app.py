import logging
import os
from pathlib import Path

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
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

PROJECT_PATH = Path(__file__).parent.parent
db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)

    # curdパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprint
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # アプリのコンフィグ設定
    # db_uri = f"mysql+pymysql://user:password@host/db_name?charset=utf8"
    db_uri = f"sqlite:///{PROJECT_PATH / 'local.sqlite'}"
    print("DB URI=", db_uri)
    app.config.from_mapping(
        SECRET_KEY="X2fbZ3h0BAk7bRXhG2CHEfW6ISBVsdz1",
        WTF_CSRF_SECRET_KEY="X2fbZ3h0BAk7bRXhG2CHEfW6ISBVsdz1",
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True,
    )
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
    app.logger.setLevel(logging.DEBUG)
    _ = DebugToolbarExtension(app)
    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    # CSRFとアプリを連携する
    csrf.init_app(app)

    return app
