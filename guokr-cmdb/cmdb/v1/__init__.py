# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint
import flask_restful as restful
import jwt
from .routes import routes
from .validators import security
from flask import request
from flask import current_app as app
from .errors import abort
from cmdb.core.db import DBsession
from cmdb.models import aws_model
@security.scopes_loader
def current_scopes():
    # token = request.cookies.get("access_token")
    # if not token:
    #     #未登录用户直接访问页面
    #      return ['guest']
    # else:
    #     try:
    #         user_token = jwt.decode(token, app.config["SECRET"])
    #         print(user_token)
    #     except jwt.ExpiredSignatureError:
    #         #用户需要重新登陆获取新的token
    #         abort('unauthorized')
    #     except jwt.ExpiredSignatureError:
    #         abort('unauthorized')
    #     else:
    #         if 'uid' not in user_token:
    #             #非法登陆
    #             abort('error_access_token')
    #         user = DBsession.query(aws_model.CmdbUser).filter_by(id=user_token["uid"]).first()
    #         if not user:
    #             #非法登陆
    #             abort('error_access_token')
    #         if user_token["authority"] == "user":
    #             return ["user", "guest"]
    #         else:
    #             return ["user", "guest", "admin"]
    return ["user", "guest", "admin"]



bp = Blueprint('v1', __name__, static_folder='static')
api = restful.Api(bp, catch_all_404s=True)

for route in routes:
    api.add_resource(route.pop('resource'), *route.pop('urls'), **route)