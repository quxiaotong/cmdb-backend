# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import datetime
from ..errors import abort
from cmdb.core.db import influxdb_client

class AwsserverEc2InstanceIpDisk(Resource):

    def get(self, instance_ip):
        ip = "'" + instance_ip + "'"
        dvalue = 24
        now = datetime.datetime.now() + datetime.timedelta(hours=-8)
        end = datetime.datetime.now() + datetime.timedelta(hours=-(8+dvalue))

        start_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"
        end_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(end,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"

        res_influx = influxdb_client.query("select %s,%s,%s,%s,%s,%s from ec2_disk where host=%s and time > %s and time < %s " %(
                                    "all_size"	, "avail_size", "device", "mount_dir", "used_percent", "used_size", ip, end_time, start_time))
        res_data = []

        for data in res_influx:
            for item in data:
                del item["time"]
                res_data.append(item)

        return res_data, 200, None
