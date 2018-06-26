# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from influxdb import InfluxDBClient
from flask import current_app as app
import re
import datetime
from cmdb.core.db import influxdb_client

class AppsApphostPointStatus(Resource):

    def get(self):
        host_ip = g.args.get("host_ip").split(":")[0]
        time_point = g.args.get("time_point")
        monitor_item = g.args.get("monitor_item")

        ip = "'" + host_ip + "'"

        monitor_point_time = datetime.datetime.strptime(time_point,"%Y-%m-%d %H:%M:%S")

        start = monitor_point_time + datetime.timedelta(minutes=-0.08)
        end = monitor_point_time + datetime.timedelta(minutes=+0.08)

        start_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(start,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"
        end_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(end,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"

        def inf_data(monitor, res_influx):
            res_data = []
            for res in res_influx:
                data = res
                pid = []
                process_name = []
                monitor_data = []
                for item in data:
                    pid.append(item["pid"])
                    process_name.append(item["process_name"])
                    monitor_data.append(float(item[monitor]))
                res_data.append(pid)
                res_data.append(process_name)
                res_data.append(monitor_data)
            return res_data

        res_data = []

        if re.search("cpu", monitor_item, flags=re.I):
            res_influx = influxdb_client.query("select %s,%s,%s from app_cpu_top where host=%s and time > %s and time < %s " %("cpu_percent","pid","process_name", ip, start_time, end_time))
            res_data = inf_data("cpu_percent",res_influx)
        elif re.search("memery", monitor_item, flags=re.I):
            res_influx = influxdb_client.query("select %s,%s,%s from app_memery_top where host=%s and time > %s and time < %s " %("memery_percent","pid","process_name", ip, start_time, end_time))
            res_data = inf_data("memery_percent",res_influx)


        return res_data, 200, None