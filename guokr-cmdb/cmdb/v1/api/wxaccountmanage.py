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

class Wxaccountmanage(Resource):

    def get(self):
        acc_obj = aws_model.WinXinAcount()
        res_acc = acc_obj.get_accunt
        return res_acc, 200, None

    def put(self):
        req_data = json.loads(json.dumps(request.form))
        use_type = req_data["use_type"]
        name = req_data["name"]
        mail = str(req_data["mail"])
        secret = str(req_data["secret"])
        type = req_data["type"]
        use_name = req_data["use_name"]
        phone = req_data["phone"]

        now = datetime.datetime.now()
        DBsession.query(aws_model.WinXinAcount).filter_by(id=id).update({
            "use_type": use_type,
            "name": name,
            "mail": mail,
            "secret": secret,
            "type": type,
            "use_name": use_name,
            "phone": phone,
            "data_update_time": now
        })
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()
            abort('add_config_error')
        else:
            acc_obj = aws_model.WinXinAcount()
            res_acc = acc_obj.get_accunt
            return res_acc, 200, None

    def post(self):
        req_data = json.loads(json.dumps(request.form))
        use_type = req_data["use_type"]
        name = req_data["name"]
        mail = str(req_data["mail"])
        secret = str(req_data["secret"])
        type = req_data["type"]
        use_name = req_data["use_name"]
        phone = req_data["phone"]
        now = datetime.datetime.now()
        account_ins = aws_model.WinXinAcount(
            use_type=use_type,
            name=name,
            mail=mail,
            secret=secret,
            type=type,
            use_name=use_name,
            phone=phone,
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
            acc_obj = aws_model.WinXinAcount()
            res_acc = acc_obj.get_accunt
            return res_acc, 200, None


    def delete(self):
        req_data = json.loads(json.dumps(request.form))
        account_id = int(req_data["account_id"])
        try:
            res = DBsession.query(aws_model.WinXinAcount).filter_by(id=account_id).first()
            setattr(res, "data_status", False)
            DBsession.commit()
        except exc.SQLAlchemyError:
            aws_model.DBsession.rollback()
        else:
            acc_obj = aws_model.WinXinAcount()
            res_acc = acc_obj.get_accunt
            return res_acc, 200, None