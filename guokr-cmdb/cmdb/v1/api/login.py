# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response
from . import Resource
from .. import schemas
import json
from cmdb.core.db import DBsession
from cmdb.models import aws_model
from ..errors import abort
import datetime
from flask import current_app as app
from sqlalchemy import exc
import jwt

class Login(Resource):
    payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365),
            'iat': datetime.datetime.utcnow(),
            'iss': 'cmdb',
            'uid': "",
            'authority': "",
        }
    def post(self):
        req_data = json.loads(json.dumps(request.form))
        account = req_data["account"]
        secret = req_data["secret"]
        user = DBsession.query(aws_model.CmdbUser).filter(aws_model.CmdbUser.account == account and aws_model.CmdbUser.data_status == True).first()
        if not user:
            abort('cmdb_user_not_found')
        elif user.secret != secret:
            abort('cmdb_user_secret_error')
        else:
            res_data = []
            res_token = {}
            self.payload["uid"] = user.id
            self.payload["authority"] = user.authority
            token = bytes.decode(jwt.encode(self.payload, app.config['SECRET'], algorithm='HS256'))
            res_token["access_token"] = token
            res_data.append(res_token)
            return res_data, 201, None


    def put(self):
        req_data = json.loads(json.dumps(request.form))
        account = req_data["account"]
        secret = req_data["secret"]
        authority = req_data["authority"]
        user = DBsession.query(aws_model.CmdbUser).filter_by(account=account).first()
        if user:
            abort('cmdb_user_exited')
        else:
            now = datetime.datetime.now()
            user_ins = aws_model.CmdbUser(
                authority=authority,
                account=account,
                secret=secret,
                data_create_time=now,
                data_status=True
            )
            aws_model.DBsession.add(user_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                aws_model.DBsession.rollback()
            else:
                uid = DBsession.query(aws_model.CmdbUser.id).filter_by(account=account).first()
                self.payload["data"]["id"] = uid
                self.payload["data"]["authority"] = authority
                token = jwt.encode(self.payload, app.config['SECRET'], algorithm='HS256')

                return token, 201, None
