# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort

class AwsserverElb(Resource):

    def get(self):
        elb_obj = aws_model.Elb()
        elb_to_api = elb_obj.elb_to_api
        if not elb_to_api:
            pass
        return elb_to_api, 200, None

