# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort

class AwsserverElasticache(Resource):

    def get(self):
        ec_obj = aws_model.Elasticache()
        ec_to_api = ec_obj.ec_to_api
        if not ec_to_api:
            pass

        return ec_to_api, 200, None

