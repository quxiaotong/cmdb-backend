import boto3
import datetime,time
class CloudWatch(object):
    def __init__(self,Monitor_Item,Identification_ID,StartTime,EndTime,Period,Show_status):
        self.MetricName=Monitor_Item
        self.Value=Identification_ID
        self.StartTime=datetime.datetime.strptime(StartTime,"%Y-%m-%d-%H-%M")
        self.EndTime=datetime.datetime.strptime(EndTime,"%Y-%m-%d-%H-%M")
        self.Period=Period
        self.Statistics=Show_status

    def data_collect(self,Aws_Service,Identification):
        Cloudwatch_Res=[]
        Cloudwatch_Keys=[
            "Timestamp",
            self.Statistics,
        ]

        cloudwatch_client=boto3.client('cloudwatch')
        cloudwatch_res=cloudwatch_client.get_metric_statistics(
            Namespace=Aws_Service,
            MetricName=self.MetricName,
            Dimensions=[
                {
                "Name":Identification,
                "Value":self.Value,
                }
            ],
        StartTime=self.StartTime,
        EndTime=self.EndTime,
        Period=int(self.Period),
        Statistics=[self.Statistics],
        )
        for item in cloudwatch_res["Datapoints"]:
            data = {key: item.get(key,'') for key in Cloudwatch_Keys}
            Cloudwatch_Res.append(data)
        for field_change in Cloudwatch_Res:
            field_change["Timestamp"]=field_change.get("Timestamp").strftime("%Y-%m-%d %H:%M")
        return Cloudwatch_Res

class Ec2_CloudWatch(CloudWatch):
    def Ec2_data_collect(self,Aws_Service="AWS/EC2",Identification="InstanceId"):
        ec2_cloudwatch_res=self.data_collect(Aws_Service,Identification)
        return ec2_cloudwatch_res

class Elb_CloudWatch(CloudWatch):
    def Elb_data_collect(self,Aws_Service="AWS/ELB",Identification="LoadBalancerName"):
        elb_cloudwatch_res=self.data_collect(Aws_Service,Identification)
        return elb_cloudwatch_res

class Rds_CloudWatch(CloudWatch):
    def Rds_data_collect(self,Aws_Service="AWS/RDS",Identification="DBInstanceIdentifier"):
        rds_cloudwatch_res=self.data_collect(Aws_Service,Identification)
        return rds_cloudwatch_res

class Redis_CloudWatch(CloudWatch):
    def Redis_data_collect(self,Aws_Service="AWS/ElastiCache",Identification="CacheClusterId"):
        redis_cloudwatch_res=self.data_collect(Aws_Service,Identification)
        return redis_cloudwatch_res

def ec2_cloudwatch_data(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus):
    ec2_cloudwatch=Ec2_CloudWatch(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus)
    ec2_cw_data=ec2_cloudwatch.Ec2_data_collect()
    print(ec2_cw_data)
    return ec2_cw_data

def elb_cloudwatch_data(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus):
    elb_cloudwatch=Elb_CloudWatch(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus)
    elb_cw_data=elb_cloudwatch.Elb_data_collect()
    print(elb_cw_data)
    return elb_cw_data

def rds_cloudwatch_data(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus):
    rds_cloudwatch=Rds_CloudWatch(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus)
    rds_cw_data=rds_cloudwatch.Rds_data_collect()
    print(rds_cw_data)
    return rds_cw_data

def redis_cloudwatch_data(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus):
    redis_cloudwatch=Redis_CloudWatch(Monitor_Item,Identification_ID,StartTime,EndTime,Period,data_showstatus)
    redis_cw_data=redis_cloudwatch.Redis_data_collect()
    print(redis_cw_data)
    return redis_cw_data

#ec2_cloudwatch_data("DiskWriteOps","i-0b9e02cfaf721e11d","2018-1-18-1-0","2018-1-18-2-0","120","Sum")

#elb_cloudwatch_data("HTTPCode_Backend_2XX","fantuan","2018-1-18-1-0","2018-1-18-2-0","120","Sum")

#rds_cloudwatch_data("SwapUsage","fantuan","2018-1-18-1-0","2018-1-18-2-0","120","Sum")

redis_cloudwatch_data("CacheHits","guokr-redis-001","2018-1-18-1-0","2018-1-18-7-0","120","Average")
