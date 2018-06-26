# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..errors import abort
from cmdb.models import aws_model

class AwsserverIamUserId(Resource):

    def delete(self, user_id):
        iam_instance = aws_model.DBsession.query(aws_model.Iam).filter(aws_model.Iam.user_id == user_id).first()
        if not iam_instance:
            abort('iam_not_found')
        aws_model.DBsession.query(aws_model.Iam).filter(aws_model.Iam.user_id == user_id).update({"data_status":False})
        aws_model.DBsession.commit()
        return {"OK":True}, 201, None