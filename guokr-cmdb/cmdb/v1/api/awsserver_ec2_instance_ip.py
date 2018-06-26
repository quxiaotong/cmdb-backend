# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model

class AwsserverEc2InstanceIp(Resource):

    def get(self, instance_ip):
        ip = instance_ip
        ec2_obj = aws_model.Ec2()
        res_ec2 = ec2_obj.detail_ec2(ip)
        res_data = []
        res_data.append(res_ec2)
        return res_data, 200, None