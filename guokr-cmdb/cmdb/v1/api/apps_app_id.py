# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.core.db import DBsession
from cmdb.models import aws_model
import re
from flask import current_app as app
import datetime
from cmdb.core.db import influxdb_client

class AppsAppId(Resource):
    def get(self, app_id):

        app_name = app_id
        res_app = []
        app_id = DBsession.query(aws_model.App.id).filter_by(name=app_name).first()
        resources = DBsession.query(aws_model.App2Aws.resource_type, aws_model.App2Aws.resource_id).filter_by(app_id=app_id).all()
        for item in resources:
            res_resource = {}
            if re.search("ec2", item[0], flags=re.I):
                res = DBsession.query(aws_model.Ec2).filter_by(id=item[1]).first()
                res_resource["resource_type"] = item[0]
                res_resource["name"] = res.name
                res_resource["private_ip"] = res.private_ip
                res_resource["standard"] = str(res.ec2_type.cpu) + "U" + "," + str(res.ec2_type.memory) + "G"
                res_resource["aws_create_time"] = res.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
                res_app.append(res_resource)

            elif re.search("redis", item[0], flags=re.I):
                res = DBsession.query(aws_model.Elasticache).filter_by(id=item[1]).first()
                res_resource["resource_type"] = item[0]
                res_resource["name"] = res.cachecluster_id
                res_resource["standard"] = str(res.ec_type.memory) + "G"
                res_resource["aws_create_time"] = res.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
                res_app.append(res_resource)

            elif re.search("rds", item[0], flags=re.I):
                res = DBsession.query(aws_model.Rds).filter_by(id=item[1]).first()
                res_resource["resource_type"] = item[0]
                res_resource["name"] = res.db_identifier
                res_resource["standard"] = str(res.rds_type.cpu) + "U" + "," + str(res.rds_type.memory) + "G"
                res_resource["aws_create_time"] = res.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
                res_app.append(res_resource)
            elif re.search("elb", item[0], flags=re.I):
                res = DBsession.query(aws_model.Elb).filter_by(id=item[1]).first()
                res_resource["resource_type"] = item[0]
                res_resource["name"] = res.loadbalancer_name
                res_resource["standard"] = "None"
                res_resource["aws_create_time"] = res.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
                res_app.append(res_resource)

        return res_app, 200, None