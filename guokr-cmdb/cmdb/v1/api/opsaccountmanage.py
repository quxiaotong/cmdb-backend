# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from ..errors import abort
from flask import request, g
from sqlalchemy import exc
from . import Resource
from .. import schemas
from cmdb.core.db import DBsession
from cmdb.models import aws_model
import json
import datetime

class Opsaccountmanage(Resource):

    def get(self):
        acc_obj = aws_model.OpsAccountManage()
        res_acc = acc_obj.get_accunt
        return res_acc, 200, None

    def put(self):
        req_data = json.loads(json.dumps(request.form))
        id = req_data["account_id"]
        platform = req_data["platform"]
        account = str(req_data["account"])
        secret = str(req_data["secret"])
        mark = req_data["mark"]
        now = datetime.datetime.now()
        DBsession.query(aws_model.OpsAccountManage).filter_by(id=id).update({
            "platform": platform,
            "account": account,
            "secret": secret,
            "mark": mark,
            "data_update_time": now
        })
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()
            abort('add_config_error')
        else:
            acc_obj = aws_model.OpsAccountManage()
            res_acc = acc_obj.get_accunt
            return res_acc, 200, None

    def post(self):
        req_data = json.loads(json.dumps(request.form))
        platform = req_data["platform"]
        account = str(req_data["account"])
        secret = str(req_data["secret"])
        mark = req_data["mark"]
        now = datetime.datetime.now()
        account_ins = aws_model.OpsAccountManage(
            platform=platform,
            account=account,
            secret=secret,
            mark=mark,
            data_update_time=now,
            data_create_time=now,
            data_status=True
        )
        aws_model.DBsession.add(account_ins)
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()
            abort('add_config_error')
        else:
            acc_obj = aws_model.OpsAccountManage()
            res_acc = acc_obj.get_accunt
            return res_acc, 200, None


    def delete(self):
        req_data = json.loads(json.dumps(request.form))
        account_ids = eval(req_data["data"])["account_id"]
        if isinstance(account_ids, int):
            account_ids = str(account_ids)
        for account_id in account_ids:
            account_id = int(account_id)
            try:
                DBsession.query(aws_model.OpsAccountManage).filter_by(id=account_id).delete()
                DBsession.commit()
            except exc.SQLAlchemyError:
                aws_model.DBsession.rollback()

        acc_obj = aws_model.OpsAccountManage()
        res_acc = acc_obj.get_accunt

        return res_acc, 200, None