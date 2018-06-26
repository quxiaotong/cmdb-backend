# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model
import datetime
import re
from cmdb.core.db import influxdb_client
import dateutil
from dateutil import parser

class AwsserverEc2InstanceIpMonitorItem(Resource):

    def get(self, instance_ip, monitor_item):
        ec2_ins_ip = instance_ip
        monitor_item = monitor_item
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

        now = datetime.datetime.now()
        end = datetime.datetime.now() + datetime.timedelta(hours=-dvalue)

        start_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"
        end_time = "'" + datetime.datetime.strptime(datetime.datetime.strftime(end,"%Y.%m.%d %H:%M:%S"),"%Y.%m.%d %H:%M:%S").isoformat() + "Z" + "'"

        id = 1
        res_cpu_data = []
        res_mem_data = []

        if re.search("cpu", monitor_item, flags=re.I):
            ip = "'" + ec2_ins_ip + "'"
            res_cpu_ec2 = []
            idle_cpu = []
            sys_cpu = []
            user_cpu = []
            res_time = []
            res_influx = influxdb_client.query("select %s,%s,%s from system_cpu where host=%s and time > %s and time < %s " %("idle_cpu", "sys_cpu","user_cpu",ip, end_time, start_time))
            for res in res_influx:
                data = res
                for item in data:
                    time = datetime.datetime.strftime(dateutil.parser.parse(item["time"]),"%Y-%m-%d %H:%M:%S")
                    idle_cpu.append(int(item['idle_cpu']))
                    sys_cpu.append(int(item['sys_cpu']))
                    user_cpu.append(int(item['user_cpu']))
                    res_time.append(time)
            res_cpu_ec2.append({"quota": "idle_cpu", "value": idle_cpu})
            res_cpu_ec2.append({"quota": "sys_cpu", "value": sys_cpu})
            res_cpu_ec2.append({"quota": "user_cpu", "value": user_cpu})
            res_cpu_ec2.append(res_time)
            res_cpu_data.append({"id": id, "host": ec2_ins_ip, "value": res_cpu_ec2, "monitor_item": "cpu"})

            return res_cpu_data, 200, None

        elif re.search("mem", monitor_item, flags=re.I):
            ip = "'" + ec2_ins_ip + "'"
            res_mem_ec2 = []
            free_mem_retio = []
            free_mem = []
            res_time = []
            res_influx = influxdb_client.query("select %s,%s from system_memery where host=%s and time > %s and time < %s " %("free_memery", "free_memery_retio", ip, end_time, start_time))
            for res in res_influx:
                data = res
                for item in data:
                    time = datetime.datetime.strftime(dateutil.parser.parse(item["time"]),"%Y-%m-%d %H:%M:%S")
                    free_mem_retio.append(item['free_memery_retio'])
                    free_mem.append(item['free_memery'])
                    res_time.append(time)
            res_mem_ec2.append({"quota": "free_memery_retio", "value": free_mem_retio})
            res_mem_ec2.append({"quota": "free_memery", "value": free_mem})
            res_mem_ec2.append(res_time)
            res_mem_data.append({"id": id, "host": ec2_ins_ip, "value": res_mem_ec2, "monitor_item": "memery"})
            return res_mem_data, 200, None