# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import g

from . import Resource
from cmdb.core import cloudwatch
from cmdb.models import aws_model
from ..errors import abort
from datetime import  datetime

class CloudwatchElbLoadbalancerName(Resource):

    def get(self, loadbalancer_name):
        identification_id = loadbalancer_name
        elb_monitor_item = g.args.get("elb_monitor_item")
        start_time = g.args.get("start_time")
        end_time = g.args.get("end_time")
        period = g.args.get("period")
        data_showstatus = g.args.get("polymerization")

        elb_instance = aws_model.DBsession.query(aws_model.Elb).filter(aws_model.Elb.data_status !="False",aws_model.Elb.loadbalancer_name == identification_id).first()
        if not elb_instance:
            abort('elb_not_found')
        if period % 60 != 0:
            abort('period_not_right')
        try:
            start_time = datetime.strptime(start_time,"%Y.%m.%d %H:%M:%S")
            end_time = datetime.strptime(end_time,"%Y.%m.%d %H:%M:%S")
        except Exception:
            abort("time_not_right")
        res_cw = cloudwatch.elb_cloudwatch_data(elb_monitor_item, identification_id, start_time, end_time, period, data_showstatus)
        return res_cw, 200, None