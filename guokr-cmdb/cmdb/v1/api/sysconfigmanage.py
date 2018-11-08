# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from sqlalchemy import exc
from . import Resource
from .. import schemas
from cmdb.models import aws_model
import json
import etcd
from flask import current_app as app
import datetime
from cmdb.core.etcd import sysconfig_pg_add,sysconfig_pg_update,access_token


client = etcd.Client(host=app.config['ETCD'], port=app.config['ETCD_PORT'])

class Sysconfigmanage(Resource):

    def get(self):
        app_name = g.args.get("app_name")
        app_obj = aws_model.App()
        res_sysconfig = app_obj.get_sysconfig(app_name)

        return res_sysconfig, 200, None


    def post(self):
        req_data = json.loads(json.dumps(request.form))
        app_name = req_data["app_name"]
        key = req_data["key"]
        value = req_data["value"]
        token = req_data["user_name"]

        user_name = access_token(token)
        app_id = aws_model.DBsession.query(aws_model.App.id).filter(aws_model.App.name == app_name).first()

        config_key = aws_model.DBsession.query(aws_model.sysconfig.key).filter(aws_model.sysconfig.app_id == app_id, aws_model.sysconfig.key == key).first()

        if not config_key:
            client.write("/services/" + app_name + "/conf/" + key, value)
            sysconfig_pg_add(app_id, user_name, key, value)
        app_obj = aws_model.App()
        res_sysconfig = app_obj.get_sysconfig(app_name)

        return res_sysconfig, 200, None

    def put(self):
        req_data = json.loads(json.dumps(request.form))
        app_name = req_data["app_name"]
        key = req_data["key"]
        value = req_data["value"]
        token = req_data["user_name"]

        user_name = access_token(token)
        app_id = aws_model.DBsession.query(aws_model.App.id).filter(aws_model.App.name == app_name).first()

        config_key = aws_model.DBsession.query(aws_model.sysconfig.key).filter(aws_model.sysconfig.app_id == app_id, aws_model.sysconfig.key == key).first()
        # config_key = aws_model.DBsession.query(aws_model.sysconfig.key).filter(aws_model.sysconfig.app_id == app_id, aws_model.sysconfig.key == key).all()

        if config_key:
            client.write("/services/" + app_name + "/conf/" + key, value)
            sysconfig_pg_update(app_id, user_name, key, value)

        app_obj = aws_model.App()
        res_sysconfig = app_obj.get_sysconfig(app_name)

        return res_sysconfig, 200, None

    def delete(self):
        req_data = json.loads(json.dumps(request.form))
        sysconfig_ids = eval(req_data["data"])["sysconfig_id"]
        if isinstance(sysconfig_ids, int):
            sysconfig_ids = str(sysconfig_ids)
        app_name = aws_model.DBsession.query(aws_model.App.name).join(aws_model.sysconfig, aws_model.sysconfig.app_id == aws_model.App.id).filter(
            aws_model.sysconfig.id == int(sysconfig_ids[0])
        ).first()
        for sysconfig_id in sysconfig_ids:
            sysconfig_id = int(sysconfig_id)
            try:
                aws_model.DBsession.query(aws_model.sysconfig).filter_by(id=sysconfig_id).delete()

                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                aws_model.DBsession.rollback()

        app_obj = aws_model.App()
        res_sysconfig = app_obj.get_sysconfig(app_name)

        return res_sysconfig, 200, None