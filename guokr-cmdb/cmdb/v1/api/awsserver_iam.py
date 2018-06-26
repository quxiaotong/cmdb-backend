# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort


class AwsserverIam(Resource):

    def get(self):
        iam_obj = aws_model.Iam()
        iam_to_api = iam_obj.iam_to_api
        if not iam_obj:
            pass
        return iam_to_api, 200, None

