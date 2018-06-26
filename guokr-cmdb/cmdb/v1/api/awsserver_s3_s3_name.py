# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..errors import abort
from cmdb.models import aws_model

class AwsserverS3S3Name(Resource):

    def delete(self, s3_name):
        s3_instance = aws_model.DBsession.query(aws_model.S3).filter(aws_model.S3.name == s3_name).first()
        if not s3_instance:
            abort('s3_not_found')
        aws_model.DBsession.query(aws_model.S3).filter(aws_model.S3.name == s3_name).update({"data_status":False})
        aws_model.DBsession.commit()
        return {"OK":True}, 201, None