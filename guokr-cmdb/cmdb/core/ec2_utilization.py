#ÈÝÁ¿¼ÆËã
import re
import datetime
from cmdb.models import aws_model
from cmdb.v1.errors import abort
from cmdb.core.db import influxdb_client
import dateutil
from dateutil import parser

def ec2_utilizat(instance_id,):
        identification_id = instance_id
        ec2_monitor_item = "CPUUtilization"
        end_time = "3d"

        dvalue = 0
        if re.search("h", end_time, flags=re.I):
            dvalue = int(end_time.split("h")[0])
        elif re.search("d", end_time, flags=re.I):
            dvalue = int(end_time.split("d")[0])*24
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
        try:
            if re.search("cpu", ec2_monitor_item, flags=re.I):
                res_influx = influxdb_client.query("select %s from cloudwatch_ec2_cpu where id=%s and time > %s and time < %s " %(ec2_monitor_item, id,end_time, start_time))
            elif re.search("net", ec2_monitor_item, flags=re.I):
                res_influx = influxdb_client.query("select %s from cloudwatch_ec2_netwolrkIn where id=%s and time > %s and time < %s " %(ec2_monitor_item, id, end_time,start_time))
        except Exception:
            return "insufficient data"
        res_time = []
        res_monitor = []
        data = []
        if not res_influx:
            return "insufficient data"
        for res in res_influx:
            data = res
        for item in data:
            time = datetime.datetime.strftime(dateutil.parser.parse(item["time"]),"%Y-%m-%d %H:%M:%S")
            res_time.append(time)
            res_monitor.append(item[ec2_monitor_item])
        res_data.append(res_time)
        res_data.append(res_monitor)

        gt_argv_one = []
        gt_argv_two = []
        first_level = 0
        utilizations = ["overmuch", "equitable", "nervous", "insufficiency"]
        utilization = ""
        argv = sum(res_data[1])//len(res_data[1])
        if argv < 35:
            first_level = 35
            utilization = "overmuch"
        elif 35 < argv < 50:
            first_level = 50
            utilization = "equitable"
        elif 50 < argv < 65:
            first_level = 65
            utilization = "nervous"
        else:
            utilization = "insufficiency"
            return utilization

        for cpu_value in res_data[1]:
            if (cpu_value - first_level) > 30:
                gt_argv_two.append(cpu_value)
            elif (cpu_value - first_level) > 15:
                gt_argv_one.append(cpu_value)

        gt_argvone_percent = len(gt_argv_one)/len(res_data[1])
        gt_argvtwo_percent = len(gt_argv_two)/len(res_data[1])


        if gt_argvtwo_percent > 0.3:
            try:
                utilization = utilizations[utilizations.index(utilization)+2]
            except Exception:
                utilization = "insufficiency"
        elif gt_argvone_percent > 0.3:
            utilization = utilizations[utilizations.index(utilization)+1]


        return utilization
