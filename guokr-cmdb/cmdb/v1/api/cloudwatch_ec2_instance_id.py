# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import g,request
from . import Resource
from cmdb.core import cloudwatch
from cmdb.models import aws_model
from ..errors import abort
import datetime
from flask import current_app as app
import re
import dateutil
from dateutil import parser
from cmdb.core.db import influxdb_client


class CloudwatchEc2InstanceId(Resource):


    def get(self, instance_id):
        identification_id = instance_id
        ec2_monitor_item = g.args.get("ec2_monitor_item")
        end_time = g.args.get("end_time")
        polymerization = g.args.get("polymerization")
        period = g.args.get("period")


        dvalue = 0
        if re.search("h", end_time, flags=re.I):
            dvalue = int(end_time.split("h")[0])
        elif re.search("d", end_time, flags=re.I):
            dvalue = int(end_time.split("d")[0])*12
        else:
            dvalue = int(end_time.split("w")[0])*168

        now = datetime.datetime.now() + datetime.timedelta(hours=-8)
        end = datetime.datetime.now() + datetime.timedelta(hours=-(8+dvalue))

        start_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"
        end_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(end,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"


        ec2_instance = aws_model.DBsession.query(aws_model.Ec2).filter(aws_model.Ec2.data_status is not False,aws_model.Ec2.instance_id == identification_id).first()
        if not ec2_instance:
            abort('ec2_not_found')
        id = "'"+identification_id+"'"


        res_data = []
        res_influx = []
        if re.search("cpu", ec2_monitor_item, flags=re.I):
            res_influx = influxdb_client.query("select %s from cloudwatch_ec2_cpu where id=%s and time > %s and time < %s " %(ec2_monitor_item, id,end_time, start_time))
        elif re.search("net", ec2_monitor_item, flags=re.I):
            res_influx = influxdb_client.query("select %s from cloudwatch_ec2_netwolrkIn where id=%s and time > %s and time < %s " %(ec2_monitor_item, id, end_time,start_time))
        res_time = []
        res_monitor = []
        data = []
        for res in res_influx:
            data = res
        for item in data:
            time = datetime.datetime.strftime(dateutil.parser.parse(item["time"]),"%Y-%m-%d %H:%M:%S")
            res_time.append(time)
            res_monitor.append(item[ec2_monitor_item])
        res_data.append(res_time)
        res_data.append(res_monitor)
        return res_data, 200, None
