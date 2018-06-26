# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model
from cmdb.core.db import DBsession
import json
from ..errors import abort
import datetime
from sqlalchemy import exc

class Cmdbaccountmanage(Resource):

    def get(self):
        cmdb_obj = aws_model.CmdbUser()
        res_acc = cmdb_obj.get_accunt
        if not res_acc:
            pass
        return res_acc, 200, None

    def post(self):
        req_data = json.loads(json.dumps(request.form))
        account = req_data["account"]
        secret = req_data["secret"]
        make_secret_value = req_data["make_secret_value"]
        authority = req_data["authority"]
        if secret != make_secret_value:
            abort("secret_not_mate")

        user = DBsession.query(aws_model.CmdbUser).filter_by(account=account).first()

        if user:
            abort("cmdb_user_exited")

        now = datetime.datetime.now()

        account_ins = aws_model.CmdbUser(
            authority=authority,
            account=account,
            secret=secret,
            data_create_time=now,
            data_status=True
        )
        aws_model.DBsession.add(account_ins)
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()
        cmdb_obj = aws_model.CmdbUser()
        res_acc = cmdb_obj.get_accunt

        return res_acc, 201, None

    def put(self):
        req_data = json.loads(json.dumps(request.form))
        secret = req_data["secret"]
        make_secret_value = req_data["make_secret_value"]
        authority = req_data["authority"]
        id = req_data["account_id"]

        if secret != make_secret_value:
            abort("secret_not_mate")

        DBsession.query(aws_model.CmdbUser).filter_by(id=id).update({
            "authority": authority,
            "secret": secret,
        })
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()

        cmdb_obj = aws_model.CmdbUser()
        res_acc = cmdb_obj.get_accunt

        return res_acc, 201, None

    def delete(self):
        req_data = json.loads(json.dumps(request.form))
        account_ids = eval(req_data["data"])["account_id"]
        if isinstance(account_ids, int):
            account_ids = str(account_ids)
        for account_id in account_ids:
            account_id = int(account_id)
            try:
                res = DBsession.query(aws_model.CmdbUser).filter_by(id=account_id).first()
                setattr(res, "data_status", False)
                DBsession.commit()
            except exc.SQLAlchemyError:
                aws_model.DBsession.rollback()

        acc_obj = aws_model.CmdbUser()
        res_acc = acc_obj.get_accunt

        return res_acc, 200, None