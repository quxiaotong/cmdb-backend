from influxdb import InfluxDBClient
import datetime
from flask import current_app as app
from cmdb.core.task.celery_base import celery
import re


@celery.task()
def cloudwatch():
    from cmdb.core.cloudwatch import ec2_cloudwatch_data
    from cmdb.core.cloudwatch import redis_cloudwatch_data
    from cmdb.core.cloudwatch import rds_cloudwatch_data
    from cmdb.models import aws_model
    from cmdb.core.db import influxdb_client
    # influxdb_client = InfluxDBClient(app.config['INFLUXDB_IP'],app.config['INFLUXDB_PORT'] , app.config['INFLUXDB_USER'], app.config['INFLUXDB_PASSWORD'], app.config['INFLUXDB_DATABASE'])
    all_ec2_id = aws_model.DBsession.query(aws_model.Ec2.instance_id).filter(aws_model.Ec2.data_status is not False).all()
    all_ec_id = aws_model.DBsession.query(aws_model.Elasticache.cachecluster_id).filter(aws_model.Elasticache.data_status is not False).all()
    all_rds_id = aws_model.DBsession.query(aws_model.Rds.db_identifier).filter(aws_model.Rds.data_status is not False).all()
    period = int(int(app.config['IF_PERIOD'])/3600)
    now = datetime.datetime.now() + datetime.timedelta(hours=-(8+period))
    end = datetime.datetime.now() + datetime.timedelta(hours=-8)
    now_time = now.strftime("%Y.%m.%d %H:%M:%S")
    end_time = end.strftime("%Y.%m.%d %H:%M:%S")
    json_body = [
        {
            "measurement": "",
            "tags": {
                "": ""
            },
            "time": "",
            "fields": {
            },
        }
    ]


    def rds_cloudwatch(monitor_item, measurement,start_time=now_time, end_time=end_time, allrds_id=all_rds_id, period=60, converge="Average"):
        for id in allrds_id:
            try:
                rds_item = rds_cloudwatch_data(monitor_item, id[0], start_time, end_time, period, converge)
            except Exception:
                pass
            else:
                for data in rds_item:
                    json_body[0]["measurement"] = measurement
                    json_body[0]["tags"]["id"] = id[0]
                    json_body[0]["time"] = data["Timestamp"]
                    if re.search("free", monitor_item, flags=re.I):
                        json_body[0]["fields"][monitor_item] = int((data["data"]/1024)/1024)
                    else:
                        json_body[0]["fields"][monitor_item] = data["data"]
                    influxdb_client.write_points(json_body)

    def redis_cloudwatch(monitor_item,measurement, start_time=now_time, end_time=end_time, allec_id=all_ec_id, period=60, converge="Average"):
        for id in allec_id:
            try:
                ec_item = redis_cloudwatch_data(monitor_item, id[0], start_time, end_time, period, converge)
            except Exception:
                pass
            else:
                for data in ec_item:
                    json_body[0]["measurement"] = measurement
                    json_body[0]["tags"]["id"] = id[0]
                    json_body[0]["time"] = data["Timestamp"]
                    if re.search("free", monitor_item, flags=re.I):
                        json_body[0]["fields"][monitor_item] = int((data["data"]/1024)/1024)
                    else:
                        json_body[0]["fields"][monitor_item] = data["data"]
                    influxdb_client.write_points(json_body)

    def ec2_cloudwatch(monitor_item, measurement, start_time=now_time, end_time=end_time, allec2_id=all_ec2_id, period=60, converge="Average"):
        for id in allec2_id:
            try:
                ec2_item = ec2_cloudwatch_data(monitor_item, id[0], start_time, end_time, period, converge)
            except Exception:
                pass
            else:
                for data in ec2_item:
                    json_body[0]["measurement"] = measurement
                    json_body[0]["tags"]["id"] = id[0]
                    json_body[0]["time"] = data["Timestamp"]
                    if re.search("cpu", monitor_item, flags=re.I):
                        json_body[0]["fields"][monitor_item] = int(data["data"]/1)
                    elif re.search("net", monitor_item, flags=re.I):
                        json_body[0]["fields"][monitor_item] = int(data["data"]/1024)
                    else:
                        json_body[0]["fields"][monitor_item] = data["data"]
                    influxdb_client.write_points(json_body)

    ec2_cloudwatch('CPUUtilization', "cloudwatch_ec2_cpu", period=300)
    ec2_cloudwatch('NetworkIn', "cloudwatch_ec2_netwolrkIn")
    redis_cloudwatch('FreeableMemory', "cloudwatch_redis_freememory")
    redis_cloudwatch('CacheHits', "cloudwatch_redis_cachehit")
    rds_cloudwatch('FreeableMemory', "cloudwatch_rds_freememory")
