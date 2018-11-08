# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model
import json

class AwsserverEc2(Resource):

    def get(self):
        page_agrs = json.loads(json.dumps(request.args))
        page_size = int(page_agrs.get("page_size", 20))
        page_index = int(page_agrs.get("page_index", 1))
        ec2_obj = aws_model.Ec2()
        try:
            res_ec2 = ec2_obj.ec2_to_api(page_size, page_index)
        except Exception as e:
            print(e)
        else:
            return res_ec2, 200, None