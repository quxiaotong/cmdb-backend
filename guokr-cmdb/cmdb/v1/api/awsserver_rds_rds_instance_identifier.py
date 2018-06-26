# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..errors import abort
from cmdb.models import aws_model


class AwsserverRdsRdsInstanceIdentifier(Resource):

    def put(self, rds_instance_identifier):
        run_status = g.args.get("status")
        rds_instance = aws_model.DBsession.query(aws_model.Rds).filter(aws_model.Rds.db_identifier == rds_instance_identifier).first()
        if not rds_instance:
            abort('rds_not_found')
        aws_model.DBsession.query(aws_model.Rds).filter(aws_model.Rds.db_identifier == rds_instance_identifier).update({"status":run_status})
        aws_model.DBsession.commit()
        db_res_rds = aws_model.DBsession.query(aws_model.Rds).filter(aws_model.Rds.db_identifier == rds_instance_identifier).first()
        res = []
        res.append(db_res_rds)
        return res, 201, None

    def delete(self, rds_instance_identifier):
        rds_instance = aws_model.DBsession.query(aws_model.Rds).filter(aws_model.Rds.db_identifier == rds_instance_identifier).first()
        if not rds_instance:
            abort('rds_not_found')
        aws_model.DBsession.query(aws_model.Rds).filter(aws_model.Rds.db_identifier == rds_instance_identifier).update({"data_status":False})
        aws_model.DBsession.commit()
        return {"OK":True}, 201, None