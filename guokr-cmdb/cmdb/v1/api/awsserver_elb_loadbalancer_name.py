# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import Resource
from ..errors import abort
from cmdb.models import aws_model

class AwsserverElbLoadbalancerName(Resource):

    def delete(self, loadbalancer_name):
        elb_instance = aws_model.DBsession.query(aws_model.Elb).filter(aws_model.Elb.loadbalancer_name == loadbalancer_name).first()
        if not elb_instance:
            abort('elb_not_found')
        aws_model.DBsession.query(aws_model.Elb).filter(aws_model.Elb.loadbalancer_name == loadbalancer_name).update({"data_status":False})
        aws_model.DBsession.commit()
        return {"OK":True}, 201, None