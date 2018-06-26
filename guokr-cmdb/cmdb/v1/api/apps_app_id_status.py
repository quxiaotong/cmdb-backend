# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import datetime
from flask import current_app as app
from influxdb import InfluxDBClient
import re
import dateutil
from dateutil import parser
from cmdb.models import aws_model
from cmdb.core.db import influxdb_client


class AppsAppIdStatus(Resource):

    def get(self, app_id):

        app_name = g.args.get("app_name")
        sys_status = g.args.get("sys_status")
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

        ec2_ins_ips = aws_model.DBsession.query(aws_model.Ec2.private_ip).\
            join(aws_model.App2Aws, aws_model.Ec2.id == aws_model.App2Aws.resource_id).\
            join(aws_model.App, aws_model.App.id == aws_model.App2Aws.app_id).\
            filter(aws_model.App.name == app_name, aws_model.App2Aws.resource_type == 'ec2').all()

        res_cpu_data = []
        res_mem_data = []
        id = 1
        if re.search("cpu", sys_status, flags=re.I):
            for ec2_ip in ec2_ins_ips:
                ip = "'" + ec2_ip[0] + "'"
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
                res_cpu_data.append({"id": id, "host": ec2_ip[0], "value": res_cpu_ec2, "monitor_item": "cpu"})
                id += 1

            return res_cpu_data, 200, None


        elif re.search("mem", sys_status, flags=re.I):
            for ec2_ip in ec2_ins_ips:
                ip = "'" + ec2_ip[0] + "'"
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
                res_mem_data.append({"id": id, "host": ec2_ip[0], "value": res_mem_ec2, "monitor_item": "memery"})
                id += 1
            return res_mem_data, 200, None