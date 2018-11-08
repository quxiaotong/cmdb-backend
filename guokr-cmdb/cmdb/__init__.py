# -*- coding: utf-8 -*-
from __future__ import absolute_import


from flask import Flask
from cmdb.config import Config
from flask_cors import *
from elasticapm.contrib.flask import ElasticAPM
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app, supports_credentials=True)
    app.config.from_object(Config)



    # APM 设定相关
    # Application Performance Management 应用程序运行时管理
    if app.config['APM_ENABLE']:
        from elasticapm.contrib.flask import ElasticAPM
        app.config['ELASTIC_APM'] = {
           # 应用名字，用于指定APM 上的应用名称，如
           'SERVICE_NAME': app.config['APM_SERVICE_NAME'],
           # 用于安全验证（暂时没用）
           'SECRET_TOKEN': app.config['APM_SERVICE_TOKEN'],
           # APM Server URL (e.g.: http://localhost:8200)
           'SERVER_URL': app.config['APM_SERVER_URL'],
           # 一般置为True, 详见文档
           'DEBUG': bool(app.config['APM_DEBUG']),
        }

        apm = ElasticAPM(app)
    # APM end

    with app.app_context():
        from cmdb import v1
        app.register_blueprint(
            v1.bp,
            url_prefix='/v1')
    return app

