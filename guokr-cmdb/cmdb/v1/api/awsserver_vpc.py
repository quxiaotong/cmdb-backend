# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort


class AwsserverVpc(Resource):

    def get(self):
        vpc_obj = aws_model.Vpc()
        vpc_to_api = vpc_obj.vpc_to_api
        if not vpc_to_api:
            pass
        return vpc_to_api, 200, None

