# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..errors import abort
from cmdb.models import aws_model

class AwsserverElasticacheCacheclusterId(Resource):

    def put(self, cachecluster_id):
        run_status = g.args.get("status")
        ec_instance = aws_model.DBsession.query(aws_model.Elasticache).filter(aws_model.Elasticache.cachecluster_id == cachecluster_id).first()
        if not ec_instance:
            abort('ec_not_found')
        aws_model.DBsession.query(aws_model.Elasticache).filter(aws_model.Elasticache.cachecluster_id == cachecluster_id).update({"status":run_status})
        aws_model.DBsession.commit()
        db_res_ec = aws_model.DBsession.query(aws_model.Elasticache).filter(aws_model.Elasticache.cachecluster_id == cachecluster_id).first()
        res = []
        res.append(db_res_ec)
        return res, 201, None

    def delete(self, cachecluster_id):
        ec_instance = aws_model.DBsession.query(aws_model.Elasticache).filter(aws_model.Elasticache.cachecluster_id == cachecluster_id).first()
        if not ec_instance:
            abort('ec_not_found')
        aws_model.DBsession.query(aws_model.Elasticache).filter(aws_model.Elasticache.cachecluster_id == cachecluster_id).update({"data_status":False})
        aws_model.DBsession.commit()

        return {"OK":True}, 201, None