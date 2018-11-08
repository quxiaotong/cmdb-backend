# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model

class AppsProjNameAppId(Resource):

    def get(self, proj_name, app_id):
        app_res = aws_model.DBsession.query(aws_model.App2Aws.listen_port, aws_model.App2Aws.host_ip, aws_model.Ec2.name,
            aws_model.Ec2.aws_create_time, aws_model.Ec2.utilization, aws_model.Ec2type.cpu, aws_model.Ec2type.memory).\
            join(aws_model.App, aws_model.App.id == aws_model.App2Aws.app_id).\
            join(aws_model.Ec2, aws_model.Ec2.private_ip == aws_model.App2Aws.host_ip).\
            join(aws_model.Ec2type, aws_model.Ec2.instance_type == aws_model.Ec2type.type).\
        filter(aws_model.App.name == app_id, aws_model.App.project == proj_name).all()
        # for ec2_ins in app_res:
        #     ec2_ins.cpu = str(ec2_ins.cpu)
        #     ec2_ins.memory = str(ec2_ins.memory)
        #     ec2_ins.aws_create_time = ec2_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
        return app_res, 200, None