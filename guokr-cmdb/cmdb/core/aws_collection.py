# -*- coding: utf-8 -*-
import boto3


Ec2_keys = ["InstanceId", "PublicIpAddress", "PrivateIpAddress", "InstanceType", "KeyName", "LaunchTime", "State", "VpcId", "Tags",]
Ec_keys = ["CacheNodeType", "CacheClusterId", "Engine", "CacheClusterCreateTime", "CacheClusterStatus"]
Elb_keys = ["LoadBalancerName", "CreatedTime", "ListenerDescriptions", "VPCId", "DNSName","Instances"]
Rds_keys = ["Engine", "DbiResourceId", "DBInstanceStatus", "StorageType", "InstanceCreateTime", "DBInstanceClass", "DBInstanceIdentifier", "DBSubnetGroup", ]
Vpc_keys = ["VpcId", "CidrBlock", "State", ]
Iam_key = ["UserName", "UserId", "CreateDate", "PasswordLastUsed", ]
Vol_keys = ["CreateTime", "Size", "State", "VolumeId", "Iops", "VolumeType", "Attachments"]

Ec2_res_keys = ["PrivateIpAddress", "PublicIpAddress", "State", "KeyName", "LaunchTime", "VpcId", "InstanceType", "Name"]
Ec2_db_keys = ["private_ip", "public_ip", "run_state", "keyname", "aws_create_time", "vpc_id", "instance_type", "name"]

Ec_res_keys = ["CacheClusterCreateTime", "CacheClusterStatus", "Engine", "CacheNodeType"]
Ec_db_keys = ["aws_create_time", "status", "engine", "cachenode_type"]

Elb_res_keys = ["LoadBalancerName", "LoadBalancerPort", "InstancePort", "CreatedTime",]
# Elb_db_keys = ["loadbalancer_name", "loadbalancer_port", "instance_port", "aws_create_time", "vpc_id"]
Elb_db_keys = ["loadbalancer_name", "loadbalancer_port", "instance_port", "aws_create_time",]


Rds_res_keys = ["DBInstanceIdentifier", "DBInstanceStatus", "Engine", "InstanceCreateTime", "DBInstanceClass", "VpcId", "StorageType"]
Rds_db_keys = ["db_identifier", "status", "engine", "aws_create_time", "instance_type", "vpc_id", "storage_type"]

Vol_res_keys = ["Size", "State", "CreateTime", "Iops","VolumeType"]
Vol_db_keys = ["size", "state", "aws_create_time", "iops", "volume_type"]

Vpc_res_keys = ["CidrBlock", "State"]
Vpc_db_keys = ["cidrblock", "status"]

Iam_res_keys = ["UserName", "PasswordLastUsed", "CreateDate"]
Iam_db_keys = ["user_name", "password_lastused", "aws_create_time"]

S3_res_keys = ["CreationDate", "Size"]
S3_db_keys = ["aws_create_time", "size"]

def ec2_collect():
    ec2_client = boto3.client('ec2')
    EC2 = []
    Ec2_Item = []
    ec2_res = ec2_client.describe_instances()
    if not ec2_res:
        return
    for reservation in ec2_res['Reservations']:
        for instance in reservation['Instances']:
            Ec2_Item.append(instance)
    for i in Ec2_Item:
        data = {key: i.get(key, '') for key in Ec2_keys}
        EC2.append(data)
    for field_change in EC2:
        field_change["State"] = field_change["State"]["Name"]
        for i in field_change["Tags"]:
            if i["Key"] == "Name":
                field_change["Name"] = i["Value"]
        field_change.pop("Tags")
    return EC2

def ec_collect():
    ec_client = boto3.client('elasticache')
    EC = []
    Ec_Item = []
    ec_res = ec_client.describe_cache_clusters()
    if not ec_res:
        return
    for cachecluster in ec_res['CacheClusters']:
        Ec_Item.append(cachecluster)
    for i in Ec_Item:
        data = {key: i.get(key, '') for key in Ec_keys}
        EC.append(data)
    return EC

def elb_collect():
    elb_client = boto3.client('elb')
    ELB = []
    Elb_Item = []
    elb_res = elb_client.describe_load_balancers()
    if not elb_res:
        return
    for loadbalancer_description in elb_res['LoadBalancerDescriptions']:
        Elb_Item.append(loadbalancer_description)
    for i in Elb_Item:
        data = {key: i.get(key, '') for key in Elb_keys}
        ELB.append(data)
    for field_change in ELB:
        field_change["LoadBalancerPort"] = field_change["ListenerDescriptions"][0]["Listener"]["LoadBalancerPort"]
        field_change["InstancePort"] = field_change["ListenerDescriptions"][0]["Listener"]["InstancePort"]
        field_change.pop("ListenerDescriptions")
    print(ELB)
    return ELB

def rds_collect():
    rds_client = boto3.client('rds')
    RDS = []
    Rds_Item = []
    rds_res = rds_client.describe_db_instances()
    if not rds_res:
        return
    for dbInstance in rds_res['DBInstances']:
            Rds_Item.append(dbInstance)
    for i in Rds_Item:
        data = {key: i.get(key, '') for key in Rds_keys}
        RDS.append(data)
    for field_change in RDS:
        db_subent_group = field_change.pop("DBSubnetGroup")
        field_change["VpcId"] = db_subent_group["VpcId"]
    return RDS

def vol_collect():
    ec2_client = boto3.client('ec2')
    VOL = []
    Vol_Item = []
    vol_res = ec2_client.describe_volumes()
    if not vol_res:
        return
    for volume in vol_res['Volumes']:
            Vol_Item.append(volume)
    for i in Vol_Item:
        data = {key: i.get(key, '') for key in Vol_keys}
        VOL.append(data)
    for field_change in VOL:
        attachments=field_change.pop("Attachments")
        try:
            field_change["InstanceId"] = attachments[0]["InstanceId"]
            field_change["Device"] = attachments[0]["Device"]
        except Exception:
            field_change["InstanceId"] = "None"
            field_change["Device"] = "None"
    return VOL

def vpc_collect():
    ec2_client = boto3.client('ec2')
    VPC = []
    Vpc_Item = []
    vpc_res = ec2_client.describe_vpcs()
    if not vpc_res:
        return
    for vpc in vpc_res['Vpcs']:
            Vpc_Item.append(vpc)
    for i in Vpc_Item:
        data = {key: i.get(key, '') for key in Vpc_keys}
        VPC.append(data)
    return VPC

def iam_collect():
    Iam_client = boto3.client('iam')
    iam_res = Iam_client.list_users()
    IAM = []
    Iam_Item = []
    if not iam_res:
        return
    for user in iam_res["Users"]:
        Iam_Item.append(user)
    for i in Iam_Item:
        data = {key: i.get(key, '') for key in Iam_key}
        IAM.append(data)
    for field_change in IAM:
        if not field_change["PasswordLastUsed"]:
            field_change["PasswordLastUsed"] = "None"
        else:
            field_change["PasswordLastUsed"] = field_change["PasswordLastUsed"].strftime("%Y-%m-%d %H:%M:%S")
    return IAM

def s3_collect():
    s3_client = boto3.client('s3')
    S3 = []
    s3_res = s3_client.list_buckets()
    if not s3_res:
        return
    for bucket in s3_res['Buckets']:
        S3.append(bucket)
    for bucket in S3:
        s3_res = s3_client.list_object_versions(Bucket = bucket["Name"])
        try:
            name = s3_res.get("Versions")[0]
        except Exception:
            pass
        finally:
            bucket["Size"] = int(name["Size"])
    return S3
