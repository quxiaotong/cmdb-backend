# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort

class AwsserverRds(Resource):

    def get(self):
        rds_obj = aws_model.Rds()
        rds_to_api = rds_obj.rds_to_api
        if not rds_to_api:
            pass
        return rds_to_api, 200, None

