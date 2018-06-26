# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from cmdb.models import aws_model
from flask import g,request
from ..errors import abort


class AwsserverVolume(Resource):

    def get(self):
        vol_obj = aws_model.Volume()
        vol_to_api = vol_obj.vol_to_api
        if not vol_to_api:
            pass
        return vol_to_api, 200, None

