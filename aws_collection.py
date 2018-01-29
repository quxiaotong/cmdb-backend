import boto3
import datetime
import model

Ec2_keys=["InstanceId","PublicIpAddress","PrivateIpAddress","InstanceType","KeyName","LaunchTime","State","VpcId",]
Ec_keys=["CacheNodeType","CacheClusterId","Engine","CacheClusterCreateTime","CacheClusterStatus"]
Elb_keys=["LoadBalancerName","CreatedTime","ListenerDescriptions","VPCId","DNSName"]
Rds_keys=["Engine","DbiResourceId","DBInstanceStatus","StorageType","InstanceCreateTime","DBInstanceClass","DBInstanceIdentifier","DBSubnetGroup",]
Vpc_keys=["VpcId","CidrBlock","State",]
Iam_key=["UserName","UserId","CreateDate","PasswordLastUsed",]
Vol_keys=["CreateTime","Size","State","VolumeId","Iops","VolumeType","Attachments"]

Ec2_res_keys=["PrivateIpAddress","PublicIpAddress","State","KeyName","LaunchTime","VpcId","InstanceType"]
Ec2_db_keys=["private_ip","public_ip","run_state","keyname","create_time","vpc_id","instance_type"]

Ec_res_keys=["CacheClusterCreateTime","CacheClusterStatus","Engine","CacheNodeType"]
Ec_db_keys=["create_time","status","engine","cachenode_type"]

Elb_res_keys=["LoadBalancerName","LoadBalancerPort","InstancePort","CreatedTime","VPCId"]
Elb_db_keys=["loadbalancer_name","loadbalancer_port","instance_port","created_time","vpc_id"]

Rds_res_keys=["DBInstanceIdentifier","DBInstanceStatus","Engine","InstanceCreateTime","DBInstanceClass","VpcId","StorageType"]
Rds_db_keys=["db_identifier","status","engine","create_time","instance_type","vpc_id","storage_type"]

Vol_res_keys=["Size","State","CreateTime","Iops","InstanceId","VolumeType"]
Vol_db_keys=["size","state","create_time","iops","ec2_instance_id","volume_type"]

Vpc_res_keys=["CidrBlock","State"]
Vpc_db_keys=["cidrblock","status"]

Iam_res_keys=["UserName","PasswordLastUsed","CreateDate"]
Iam_db_keys=["user_name","password_lastused","create_date"]

S3_res_keys=["CreationDate","Size"]
S3_db_keys=["creation_date","size"]

def ec2_collect():
    ec2_client=boto3.client('ec2')
    EC2=[]
    Ec2_Item=[]
    ec2_res=ec2_client.describe_instances()
    for instance in ec2_res['Reservations']:
        for item in instance['Instances']:
            Ec2_Item.append(item)
    for i in Ec2_Item:
        data = {key: i.get(key,'') for key in Ec2_keys}
        EC2.append(data)
    for field_change in EC2:
        field_change["LaunchTime"]=field_change.get("LaunchTime").strftime("%Y-%m-%d")
        field_change["State"]=field_change["State"]["Name"]
    return(EC2)
def ec_collect():
    ec_client=boto3.client('elasticache')
    EC=[]
    Ec_Item=[]
    ec_res=ec_client.describe_cache_clusters()
    for item in ec_res['CacheClusters']:
        Ec_Item.append(item)
    for i in Ec_Item:
        data = {key: i.get(key,'') for key in Ec_keys}
        EC.append(data)
    for field_change in EC:
        field_change["CacheClusterCreateTime"]=field_change.get("CacheClusterCreateTime").strftime("%Y-%m-%d")
    return(EC)
def elb_collect():
    elb_client = boto3.client('elb')
    ELB=[]
    Elb_Item=[]
    elb_res=elb_client.describe_load_balancers()
    for item in elb_res['LoadBalancerDescriptions']:
        Elb_Item.append(item)
    for i in Elb_Item:
        data = {key: i.get(key,'') for key in Elb_keys}
        ELB.append(data)
    for field_change in ELB:
        field_change["CreatedTime"]=field_change.get("CreatedTime").strftime("%Y-%m-%d")
        field_change["LoadBalancerPort"]=field_change.get("ListenerDescriptions")[0]["Listener"]["LoadBalancerPort"]
        field_change["InstancePort"]=field_change.get("ListenerDescriptions")[0]["Listener"]["InstancePort"]
        field_change.pop("ListenerDescriptions")
    return ELB
def rds_collect():
    rds_client=boto3.client('rds')
    RDS=[]
    Rds_Item=[]
    rds_res=rds_client.describe_db_instances()
    for item in rds_res['DBInstances']:
            Rds_Item.append(item)
    for i in Rds_Item:
        data = {key: i.get(key,'') for key in Rds_keys}
        RDS.append(data)
    for field_change in RDS:
        field_change["InstanceCreateTime"]=field_change.get("InstanceCreateTime").strftime("%Y-%m-%d")
        field_change["VpcId"]=field_change.get("DBSubnetGroup")["VpcId"]
        field_change.pop("DBSubnetGroup")
    return(RDS)
def vol_collect():
    ec2_client=boto3.client('ec2')
    VOL=[]
    Vol_Item=[]
    vol_res=ec2_client.describe_volumes()
    for item in vol_res['Volumes']:
            Vol_Item.append(item)
    for i in Vol_Item:
        data = {key: i.get(key,'') for key in Vol_keys}
        VOL.append(data)
    for field_change in VOL:
        field_change["CreateTime"]=field_change.get("CreateTime").strftime("%Y-%m-%d")
        field_change["Size"]=str(field_change["Size"])+"G"
        if not field_change['Attachments']:
            field_change["InstanceId"]="None"
        else:
            field_change["InstanceId"]=field_change["Attachments"][0]["InstanceId"]
        field_change.pop("Attachments")
    return VOL
def vpc_collect():
    ec2_client=boto3.client('ec2')
    VPC=[]
    Vpc_Item=[]
    vpc_res=ec2_client.describe_vpcs()
    for item in vpc_res['Vpcs']:
            Vpc_Item.append(item)
    for i in Vpc_Item:
        data = {key: i.get(key,'') for key in Vpc_keys}
        VPC.append(data)
    return(VPC)
def iam_collect():
    Iam_client = boto3.client('iam')
    Iam_res=Iam_client.list_users()
    IAM=[]
    Iam_Item=[]
    for item in Iam_res["Users"]:
        Iam_Item.append(item)
    for i in Iam_Item:
        data = {key: i.get(key,'') for key in Iam_key}
        IAM.append(data)
    for field_change in IAM:
        field_change["CreateDate"]=field_change.get("CreateDate").strftime("%Y-%m-%d")
        if field_change.get("PasswordLastUsed"):
            field_change["PasswordLastUsed"]=field_change.get("PasswordLastUsed").strftime("%Y-%m-%d")
        else:
            field_change["PasswordLastUsed"]="None"
    return IAM
def s3_collect():
    s3_client=boto3.client('s3')
    S3=[]
    s3_res=s3_client.list_buckets()
    for item in s3_res['Buckets']:
        S3.append(item)
    for create_time in S3:
        create_time["CreationDate"]=create_time.get("CreationDate").strftime("%Y-%m-%d")
    for bucket in S3:
        s3_res=s3_client.list_object_versions(Bucket=bucket["Name"])
        try:
            name=s3_res.get("Versions")[0]
        except Exception as e:
            pass
        finally:
            bucket["Size"]=str(name["Size"])+"B"
    return S3


def ec2data_to_db():
    ec2_data=ec2_collect()
    for item in ec2_data:
        res=model.DBsession.query(model.Ec2).filter_by(instance_id=item["InstanceId"]).first()
        if not res:
            ec2_type_obj = model.DBsession.query(model.Ec2type).filter_by(type=item["InstanceType"]).first()
            data=model.Ec2(instance_id=item["InstanceId"],
                       private_ip=item["PrivateIpAddress"],
                       public_ip=item["PublicIpAddress"],
                       run_state=item["State"],
                       keyname=item["KeyName"],
                       create_time=item["LaunchTime"],
                       vpc_id=item["VpcId"],
                       instance_type=ec2_type_obj.type
                           )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Ec2_res_keys,Ec2_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res, i2, item[i1])
            model.DBsession.commit()
def ecdata_to_db():
    ec_data=ec_collect()
    for item in ec_data:
        res=model.DBsession.query(model.Elasticache).filter_by(cachecluster_id=item["CacheClusterId"]).first()
        if not res:
            ec_type_obj=model.DBsession.query(model.Ectype).filter_by(type=item["CacheNodeType"]).first()
            data=model.Elasticache(cachecluster_id=item["CacheClusterId"],
                               create_time=item["CacheClusterCreateTime"],
                               status=item["CacheClusterStatus"],
                               engine=item["Engine"],
                               cachenode_type=ec_type_obj.type
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Ec_res_keys,Ec_db_keys):
                setattr(res, i2, item[i1])
            model.DBsession.commit()
def elbdata_to_db():
    elb_data=elb_collect()
    for item in elb_data:
        res=model.DBsession.query(model.Elb).filter_by(dns_name=item["DNSName"]).first()
        if not res:
            data=model.Elb(loadbalancer_name=item["LoadBalancerName"],
                       loadbalancer_port=item["LoadBalancerPort"],
                       instance_port=item["InstancePort"],
                       created_time=item["CreatedTime"],
                       vpc_id=item["VPCId"],
                       dns_name=item["DNSName"]
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Elb_res_keys,Elb_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res, i2, item[i1])
            model.DBsession.commit()
def rdsdata_to_db():
    rds_data=rds_collect()
    for item in rds_data:
        res=model.DBsession.query(model.Rds).filter_by(resource_id=item["DbiResourceId"]).first()
        if not res:
            rds_type_obj= model.DBsession.query(model.Rdstype).filter_by(type=item["DBInstanceClass"]).first()
            data=model.Rds(db_identifier=item["DBInstanceIdentifier"],
                       status=item["DBInstanceStatus"],
                       engine=item["Engine"],
                       resource_id=item["DbiResourceId"],
                       create_time=item["InstanceCreateTime"],
                       instance_type=rds_type_obj.type,
                       vpc_id=item["VpcId"],
                       storage_type=item["StorageType"]
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Rds_res_keys,Rds_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res,i2,item[i1])
            model.DBsession.commit()
def voldata_to_db():
    vol_data=vol_collect()
    for item in vol_data:
        res=model.DBsession.query(model.Volume).filter_by(volume_id=item["VolumeId"]).first()
        if not res:
            ec2_id_obj= model.DBsession.query(model.Ec2).filter_by(instance_id=item["InstanceId"]).first()
            data=model.Volume(volume_id=item["VolumeId"],
                       size=item["Size"],
                       state=item["State"],
                       create_time=item["CreateTime"],
                       iops=item["Iops"],
                       ec2_instance_id=ec2_id_obj.instance_id,
                       volume_type=item["VolumeType"]
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Vol_res_keys,Vol_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res,i2,item[i1])
            model.DBsession.commit()
def vpcdata_to_db():
    vpc_data=vpc_collect()
    for item in vpc_data:
        res=model.DBsession.query(model.Vpc).filter_by(vpc_id=item["VpcId"]).first()
        if not res:
            data=model.Vpc(vpc_id=item["VpcId"],
                       cidrblock=item["CidrBlock"],
                       status=item["State"]
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Vpc_res_keys,Vpc_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res, i2, item[i1])
            model.DBsession.commit()
def iamdata_to_db():
    iam_data=iam_collect()
    for item in iam_data:
        res=model.DBsession.query(model.Iam).filter_by(user_id=item["UserId"]).first()
        if not res:
            data=model.Iam(user_id=item["UserId"],
                       user_name=item["UserName"],
                       password_lastused=item["PasswordLastUsed"],
                       create_date=item["CreateDate"]
             )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(Iam_res_keys,Iam_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res, i2, item[i1])
            model.DBsession.commit()
def s3data_to_db():
    s3_data=s3_collect()
    for item in s3_data:
        res=model.DBsession.query(model.S3).filter_by(name=item["Name"]).first()
        if not res:
            data=model.S3(creation_date=item["CreationDate"],
                      name=item["Name"],
                      size=item["Size"]
            )
            model.DBsession.add(data)
            model.DBsession.commit()
        else:
            for i1,i2 in zip(S3_res_keys,S3_db_keys):
                if not item[i1] == getattr(res, i2):
                    setattr(res, i2, item[i1])
            model.DBsession.commit()
def alldata_to_db():
    iamdata_to_db()
    s3data_to_db()
    vpcdata_to_db()
    elbdata_to_db()
    ec2data_to_db()
    rdsdata_to_db()
    ecdata_to_db()
    voldata_to_db()

alldata_to_db()