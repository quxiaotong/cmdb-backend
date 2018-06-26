# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.awsserver_ec2_instance_ip import AwsserverEc2InstanceIp
from .api.cloudwatch_elb_loadbalancer_name import CloudwatchElbLoadbalancerName
from .api.login import Login
from .api.apps_app_name_zabbix import AppsAppNameZabbix
from .api.apps_app_id_status import AppsAppIdStatus
from .api.awsserver_elasticache import AwsserverElasticache
from .api.awsserver_ec2 import AwsserverEc2
from .api.awsserver_elb import AwsserverElb
from .api.cloudwatch_elasticache_cachecluster_id import CloudwatchElasticacheCacheclusterId
from .api.awsserver_s3 import AwsserverS3
from .api.cloudwatch_rds_instance_identifier import CloudwatchRdsInstanceIdentifier
from .api.cloudwatch_ec2_instance_id import CloudwatchEc2InstanceId
from .api.awsserver_ec2_instance_ip_disk import AwsserverEc2InstanceIpDisk
from .api.awsserver_iam_user_id import AwsserverIamUserId
from .api.apps_app_id import AppsAppId
from .api.cmdbaccountmanage import Cmdbaccountmanage
from .api.awsserver_ec2_instance_ip_monitor_item import AwsserverEc2InstanceIpMonitorItem
from .api.awsserver_ec2_instance_ip_point_status import AwsserverEc2InstanceIpPointStatus
from .api.awsserver_elb_loadbalancer_name import AwsserverElbLoadbalancerName
from .api.awsserver_iam import AwsserverIam
from .api.awsserver_volume import AwsserverVolume
from .api.awsserver_rds import AwsserverRds
from .api.apps_apphost_point_status import AppsApphostPointStatus
from .api.awsserver_elasticache_cachecluster_id import AwsserverElasticacheCacheclusterId
from .api.awsserver_vpc import AwsserverVpc
from .api.awsserver_s3_s3_name import AwsserverS3S3Name
from .api.awsserver_volume_volume_id import AwsserverVolumeVolumeId
from .api.awsserver_rds_rds_instance_identifier import AwsserverRdsRdsInstanceIdentifier
from .api.wxaccountmanage import Wxaccountmanage
from .api.apps_zabbix_status import AppsZabbixStatus
from .api.opsaccountmanage import Opsaccountmanage


routes = [
    dict(resource=AwsserverEc2InstanceIp, urls=['/awsserver/ec2/<instance_ip>'], endpoint='awsserver_ec2_instance_ip'),
    dict(resource=CloudwatchElbLoadbalancerName, urls=['/cloudwatch/elb/<loadbalancer_name>'], endpoint='cloudwatch_elb_loadbalancer_name'),
    dict(resource=Login, urls=['/login'], endpoint='login'),
    dict(resource=AppsAppNameZabbix, urls=['/apps/<app_name>/zabbix'], endpoint='apps_app_name_zabbix'),
    dict(resource=AppsAppIdStatus, urls=['/apps/<app_id>/status'], endpoint='apps_app_id_status'),
    dict(resource=AwsserverElasticache, urls=['/awsserver/elasticache'], endpoint='awsserver_elasticache'),
    dict(resource=AwsserverEc2, urls=['/awsserver/ec2'], endpoint='awsserver_ec2'),
    dict(resource=AwsserverElb, urls=['/awsserver/elb'], endpoint='awsserver_elb'),
    dict(resource=CloudwatchElasticacheCacheclusterId, urls=['/cloudwatch/elasticache/<cachecluster_id>'], endpoint='cloudwatch_elasticache_cachecluster_id'),
    dict(resource=AwsserverS3, urls=['/awsserver/s3'], endpoint='awsserver_s3'),
    dict(resource=CloudwatchRdsInstanceIdentifier, urls=['/cloudwatch/rds/<instance_identifier>'], endpoint='cloudwatch_rds_instance_identifier'),
    dict(resource=CloudwatchEc2InstanceId, urls=['/cloudwatch/ec2/<instance_id>'], endpoint='cloudwatch_ec2_instance_id'),
    dict(resource=AwsserverEc2InstanceIpDisk, urls=['/awsserver/ec2/<instance_ip>/disk'], endpoint='awsserver_ec2_instance_ip_disk'),
    dict(resource=AwsserverIamUserId, urls=['/awsserver/iam/<user_id>'], endpoint='awsserver_iam_user_id'),
    dict(resource=AppsAppId, urls=['/apps/<app_id>'], endpoint='apps_app_id'),
    dict(resource=Cmdbaccountmanage, urls=['/cmdbaccountmanage'], endpoint='cmdbaccountmanage'),
    dict(resource=AwsserverEc2InstanceIpMonitorItem, urls=['/awsserver/ec2/<instance_ip>/<monitor_item>'], endpoint='awsserver_ec2_instance_ip_monitor_item'),
    dict(resource=AwsserverEc2InstanceIpPointStatus, urls=['/awsserver/ec2/<instance_ip>/point_status'], endpoint='awsserver_ec2_instance_ip_point_status'),
    dict(resource=AwsserverElbLoadbalancerName, urls=['/awsserver/elb/<loadbalancer_name>'], endpoint='awsserver_elb_loadbalancer_name'),
    dict(resource=AwsserverIam, urls=['/awsserver/iam'], endpoint='awsserver_iam'),
    dict(resource=AwsserverVolume, urls=['/awsserver/volume'], endpoint='awsserver_volume'),
    dict(resource=AwsserverRds, urls=['/awsserver/rds'], endpoint='awsserver_rds'),
    dict(resource=AppsApphostPointStatus, urls=['/apps/apphost/point_status'], endpoint='apps_apphost_point_status'),
    dict(resource=AwsserverElasticacheCacheclusterId, urls=['/awsserver/elasticache/<cachecluster_id>'], endpoint='awsserver_elasticache_cachecluster_id'),
    dict(resource=AwsserverVpc, urls=['/awsserver/vpc'], endpoint='awsserver_vpc'),
    dict(resource=AwsserverS3S3Name, urls=['/awsserver/s3/<s3_name>'], endpoint='awsserver_s3_s3_name'),
    dict(resource=AwsserverVolumeVolumeId, urls=['/awsserver/volume/<volume_id>'], endpoint='awsserver_volume_volume_id'),
    dict(resource=AwsserverRdsRdsInstanceIdentifier, urls=['/awsserver/rds/<rds_instance_identifier>'], endpoint='awsserver_rds_rds_instance_identifier'),
    dict(resource=Wxaccountmanage, urls=['/wxaccountmanage'], endpoint='wxaccountmanage'),
    dict(resource=AppsZabbixStatus, urls=['/apps/zabbix/status'], endpoint='apps_zabbix_status'),
    dict(resource=Opsaccountmanage, urls=['/opsaccountmanage'], endpoint='opsaccountmanage'),
]