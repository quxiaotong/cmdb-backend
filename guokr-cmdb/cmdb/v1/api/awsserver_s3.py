# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort

class AwsserverS3(Resource):

    def get(self):
        s3_obj = aws_model.S3()
        s3_to_api = s3_obj.s3_to_api
        if not s3_to_api:
            pass
        return s3_to_api, 200, None
