# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from cmdb.config import Config
from flask_cors import *


def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)

    with app.app_context():
        from cmdb import v1
        app.register_blueprint(
            v1.bp,
            url_prefix='/v1')
    return app

