# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsElasticache = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'cachecluster_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'engine': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'memory_num': {'type': 'integer'}, 'id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'cachenode_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'status': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}}}, 'type': 'array'}
DefinitionsVolume = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'state': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'ec2_instance_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'volume_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'device': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}, 'volume_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'iops': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'size': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'ec2_instance_name': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsVpc = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'vpc_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'cidrblock': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'status': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}}}, 'type': 'array'}
DefinitionsOpsaccount = {'items': {'properties': {'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'mark': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'secret': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'account': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'platform': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsElb = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'loadbalancer_port': {'type': 'integer'}, 'instance_port': {'type': 'integer'}, 'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'vpc_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'dns_name': {'maxLength': 128, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}, 'loadbalancer_name': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsS3 = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'aws_creation_date': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'size': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'name': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}}}, 'type': 'array'}
DefinitionsCmdb_user_get = {'items': {'properties': {'authority': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'id': {'type': 'integer'}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'account': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsOpsconfigmanage_data = {'required': ['account', 'secret'], 'properties': {'secret': {'type': 'string'}, 'platform': {'type': 'string'}, 'account': {'type': 'string'}, 'mark': {'type': 'string'}}}
DefinitionsCloudwatch_test = {'type': 'list'}
DefinitionsDisk = {'items': {'properties': {'used_size': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'all_size': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'mount_dir': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'device': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'avail_size': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'used_percent': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsCloudwatch = {'items': {'properties': {'DatabaseConnections': {'type': 'float'}, 'CPUUtilization': {'type': 'float'}, 'SwapUsage': {'type': 'float'}, 'RequestCount': {'type': 'float'}, 'NetworkIn': {'type': 'float'}, 'time': {'type': 'string'}, 'FreeableMemory': {'type': 'float'}, 'HTTPCode_Backend_5XX': {'type': 'float'}}}, 'type': 'array'}
DefinitionsEc2 = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'keyname': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'instance_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'memory_num': {'type': 'integer'}, 'instance_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'public_ip': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'private_ip': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'run_state': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'cpu_num': {'type': 'integer'}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}, 'vpc_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'name': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsApps = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'resource_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'private_ip': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'name': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'standard': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsWxaccount = {'items': {'required': ['use_type', 'name', 'type', 'mail', 'secret', 'use_name', 'phone'], 'properties': {'type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'use_name': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'mail': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'secret': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'use_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'phone': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'name': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}
DefinitionsError = {'properties': {'message': {'type': 'string'}, 'error_code': {'type': 'string'}, 'text': {'type': 'string'}}}
DefinitionsCmdbaccount = {'required': ['account', 'secret'], 'properties': {'make_secret': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'authority': {'enum': ['admin', 'user'], 'type': 'string', 'description': '用户权限身份'}, 'secret': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'account': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}
DefinitionsIam = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'create_date': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'password_lastused': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'user_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'user_name': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}}}, 'type': 'array'}
DefinitionsToken = {'items': {'properties': {'access_token': {'type': 'string'}}}, 'type': 'array'}
DefinitionsRds = {'items': {'properties': {'aws_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_create_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'engine': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'memory_num': {'type': 'integer'}, 'storage_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'db_identifier': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'id': {'type': 'integer'}, 'data_update_time': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'cpu_num': {'type': 'integer'}, 'status': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'data_status': {'maxLength': 64, 'type': 'boolean', 'minLength': 1}, 'resource_id': {'maxLength': 64, 'type': 'string', 'minLength': 1}, 'instance_type': {'maxLength': 64, 'type': 'string', 'minLength': 1}}}, 'type': 'array'}

validators = {
    ('cloudwatch_elb_loadbalancer_name', 'GET'): {'args': {'required': ['elb_monitor_item', 'start_time', 'end_time', 'period', 'polymerization'], 'properties': {'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'start_time': {'type': 'string', 'description': '获得监控数据的起始时间'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'elb_monitor_item': {'type': 'string', 'enum': ['UnHealthyHostCount', 'RequestCount', 'Latency', 'HealthyHostCount', 'BackendConnectionErrors', 'HTTPCode_Backend_5XX', 'HTTPCode_ELB_5XX', 'HTTPCode_Backend_4XX'], 'description': '监控项'}, 'polymerization': {'type': 'string', 'enum': ['Average', 'Minimum', 'Maximum'], 'description': '数据的聚合函数'}}}},
    ('login', 'POST'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('apps_app_name_zabbix', 'GET'): {'args': {'required': [], 'properties': {'zab_app_webitem': {'required': False, 'type': 'string', 'description': 'zabbix应用app的监控项'}, 'time_point': {'required': False, 'type': 'string', 'description': 'app运行状态的时间点'}}}},
    ('apps_app_id_status', 'GET'): {'args': {'required': ['app_name', 'sys_status', 'end_time', 'polymerization', 'period'], 'properties': {'sys_status': {'enum': ['cpu', 'memery'], 'type': 'string', 'description': '监控项'}, 'polymerization': {'enum': ['Average', 'Minimum', 'Maximum'], 'type': 'string', 'description': '数据的聚合函数'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'app_name': {'type': 'string', 'description': '业务线名字'}}}},
    ('awsserver_ec2', 'GET'): {'args': {'required': [], 'properties': {'每页的行数': {'default': 1, 'type': 'string', 'required': False, 'description': '显示每页行数'}, '页数': {'default': 20, 'type': 'string', 'required': False, 'description': '显示列表分页数'}}}},
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): {'args': {'required': ['elasticache_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'elasticache_monitor_item': {'enum': ['BytesUsedForCache', 'CacheHits', 'CacheMisses', 'CPUUtilization', 'CurrConnections', 'CurrItems', 'FreeableMemory', 'Reclaimed', 'NetworkBytesIn'], 'type': 'string', 'description': '监控项'}, 'polymerization': {'enum': ['Average', 'Minimum', 'Maximum'], 'type': 'string', 'description': '数据的聚合函数'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}}}},
    ('cloudwatch_rds_instance_identifier', 'GET'): {'args': {'required': ['rds_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'polymerization': {'type': 'string', 'enum': ['Average', 'Minimum', 'Maximum'], 'description': '数据的聚合函数'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'rds_monitor_item': {'type': 'string', 'enum': ['FreeableMemory', 'FreeStorageSpace', 'ReadIOPS', 'ReadLatency', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'SwapUsage', 'WriteIOPS', 'WriteLatency', 'DatabaseConnections'], 'description': '监控项'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}}}},
    ('cloudwatch_ec2_instance_id', 'GET'): {'args': {'required': ['ec2_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'polymerization': {'enum': ['Average', 'Minimum', 'Maximum'], 'type': 'string', 'description': '数据的聚合函数'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'ec2_monitor_item': {'enum': ['CPUUtilization', 'DiskReadBytes', 'DiskReadOps', 'DiskWriteBytes', 'DiskWriteOps', 'NetworkIn', 'NetworkOut'], 'type': 'string', 'description': '监控项'}}}},
    ('cmdbaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('cmdbaccountmanage', 'PUT'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('cmdbaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'opsaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): {'args': {'required': ['end_time', 'polymerization', 'period'], 'properties': {'polymerization': {'enum': ['Average', 'Minimum', 'Maximum'], 'type': 'string', 'description': '数据的聚合函数'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}}}},
    ('awsserver_ec2_instance_ip_point_status', 'GET'): {'args': {'required': ['monitor_item'], 'properties': {'monitor_item': {'type': 'string', 'enum': ['cpu', 'memery'], 'description': 'app的监控项'}, 'time_point': {'required': False, 'type': 'string', 'description': 'app运行状态的时间点'}}}},
    ('apps_apphost_point_status', 'GET'): {'args': {'required': ['host_ip', 'monitor_item'], 'properties': {'host_ip': {'type': 'string', 'description': 'app运行的服务器ip'}, 'monitor_item': {'type': 'string', 'enum': ['cpu', 'memery'], 'description': 'app的监控项'}, 'time_point': {'required': False, 'type': 'string', 'description': 'app运行状态的时间点'}}}},
    ('awsserver_elasticache_cachecluster_id', 'PUT'): {'args': {'required': ['status'], 'properties': {'status': {'type': 'string'}}}},
    ('awsserver_volume_volume_id', 'PUT'): {'args': {'required': ['state'], 'properties': {'state': {'type': 'string'}}}},
    ('awsserver_rds_rds_instance_identifier', 'PUT'): {'args': {'required': ['status'], 'properties': {'status': {'type': 'string'}}}},
    ('wxaccountmanage', 'PUT'): {'form': {'required': ['account_id'], 'properties': {'account_id': {'type': 'string'}, 'wxconfig_data': {'schema': DefinitionsWxaccount}}}},
    ('wxaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'wxaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('wxaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'wxconfig_data': {'schema': DefinitionsWxaccount}}}},
    ('opsaccountmanage', 'PUT'): {'form': {'required': ['account_id'], 'properties': {'account_id': {'type': 'string'}, 'config_data': {'schema': DefinitionsOpsconfigmanage_data}}}},
    ('opsaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'opsaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('opsaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'config_data': {'schema': DefinitionsOpsconfigmanage_data}}}},
}

filters = {
    ('awsserver_ec2_instance_ip', 'GET'): {200: {'headers': None, 'schema': DefinitionsEc2}},
    ('cloudwatch_elb_loadbalancer_name', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch}},
    ('login', 'POST'): {200: {'headers': None, 'schema': DefinitionsToken}},
    ('apps_app_name_zabbix', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('apps_app_id_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_elasticache', 'GET'): {200: {'headers': None, 'schema': DefinitionsElasticache}},
    ('awsserver_ec2', 'GET'): {200: {'headers': None, 'schema': DefinitionsEc2}},
    ('awsserver_elb', 'GET'): {200: {'headers': None, 'schema': DefinitionsElb}},
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_s3', 'GET'): {200: {'headers': None, 'schema': DefinitionsS3}},
    ('cloudwatch_rds_instance_identifier', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('cloudwatch_ec2_instance_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_ec2_instance_ip_disk', 'GET'): {200: {'headers': None, 'schema': DefinitionsDisk}},
    ('awsserver_iam_user_id', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('apps_app_id', 'GET'): {200: {'headers': None, 'schema': DefinitionsApps}},
    ('cmdbaccountmanage', 'GET'): {200: {'headers': None, 'schema': DefinitionsCmdb_user_get}},
    ('cmdbaccountmanage', 'POST'): {200: {'headers': None, 'schema': DefinitionsCmdb_user_get}},
    ('cmdbaccountmanage', 'PUT'): {200: {'headers': None, 'schema': DefinitionsCmdb_user_get}},
    ('cmdbaccountmanage', 'DELETE'): {200: {'headers': None, 'schema': DefinitionsCmdb_user_get}},
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_ec2_instance_ip_point_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_elb_loadbalancer_name', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('awsserver_iam', 'GET'): {200: {'headers': None, 'schema': DefinitionsIam}},
    ('awsserver_volume', 'GET'): {200: {'headers': None, 'schema': DefinitionsVolume}},
    ('awsserver_rds', 'GET'): {200: {'headers': None, 'schema': DefinitionsRds}},
    ('apps_apphost_point_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('awsserver_elasticache_cachecluster_id', 'PUT'): {201: {'headers': None, 'schema': DefinitionsElasticache}},
    ('awsserver_elasticache_cachecluster_id', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('awsserver_vpc', 'GET'): {200: {'headers': None, 'schema': DefinitionsVpc}},
    ('awsserver_s3_s3_name', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('awsserver_volume_volume_id', 'PUT'): {201: {'headers': None, 'schema': DefinitionsVolume}},
    ('awsserver_volume_volume_id', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('awsserver_rds_rds_instance_identifier', 'PUT'): {201: {'headers': None, 'schema': DefinitionsRds}},
    ('awsserver_rds_rds_instance_identifier', 'DELETE'): {201: {'headers': None, 'schema': DefinitionsSuccess}},
    ('wxaccountmanage', 'GET'): {200: {'headers': None, 'schema': DefinitionsWxaccount}},
    ('wxaccountmanage', 'PUT'): {200: {'headers': None, 'schema': DefinitionsWxaccount}},
    ('wxaccountmanage', 'DELETE'): {200: {'headers': None, 'schema': DefinitionsWxaccount}},
    ('wxaccountmanage', 'POST'): {200: {'headers': None, 'schema': DefinitionsWxaccount}},
    ('apps_zabbix_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsCloudwatch_test}},
    ('opsaccountmanage', 'GET'): {200: {'headers': None, 'schema': DefinitionsOpsaccount}},
    ('opsaccountmanage', 'PUT'): {200: {'headers': None, 'schema': DefinitionsOpsaccount}},
    ('opsaccountmanage', 'DELETE'): {200: {'headers': None, 'schema': DefinitionsOpsaccount}},
    ('opsaccountmanage', 'POST'): {200: {'headers': None, 'schema': DefinitionsOpsaccount}},
}

scopes = {
    ('awsserver_ec2_instance_ip', 'GET'): ['user'],
    ('cloudwatch_elb_loadbalancer_name', 'GET'): ['user'],
    ('apps_app_name_zabbix', 'GET'): ['user'],
    ('apps_app_id_status', 'GET'): ['user'],
    ('awsserver_elasticache', 'GET'): ['user'],
    ('awsserver_ec2', 'GET'): ['user'],
    ('awsserver_elb', 'GET'): ['user'],
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): ['user'],
    ('awsserver_s3', 'GET'): ['user'],
    ('cloudwatch_rds_instance_identifier', 'GET'): ['user'],
    ('cloudwatch_ec2_instance_id', 'GET'): ['user'],
    ('awsserver_ec2_instance_ip_disk', 'GET'): ['user'],
    ('awsserver_iam_user_id', 'DELETE'): ['admin'],
    ('apps_app_id', 'GET'): ['user'],
    ('cmdbaccountmanage', 'GET'): ['admin'],
    ('cmdbaccountmanage', 'POST'): ['admin'],
    ('cmdbaccountmanage', 'PUT'): ['admin'],
    ('cmdbaccountmanage', 'DELETE'): ['admin'],
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): ['user'],
    ('awsserver_ec2_instance_ip_point_status', 'GET'): ['user'],
    ('awsserver_elb_loadbalancer_name', 'DELETE'): ['admin'],
    ('awsserver_iam', 'GET'): ['user'],
    ('awsserver_volume', 'GET'): ['user'],
    ('awsserver_rds', 'GET'): ['user'],
    ('apps_apphost_point_status', 'GET'): ['user'],
    ('awsserver_elasticache_cachecluster_id', 'PUT'): ['user'],
    ('awsserver_elasticache_cachecluster_id', 'DELETE'): ['admin'],
    ('awsserver_vpc', 'GET'): ['user'],
    ('awsserver_s3_s3_name', 'DELETE'): ['admin'],
    ('awsserver_volume_volume_id', 'PUT'): ['admin'],
    ('awsserver_volume_volume_id', 'DELETE'): ['user'],
    ('awsserver_rds_rds_instance_identifier', 'PUT'): ['user'],
    ('awsserver_rds_rds_instance_identifier', 'DELETE'): ['admin'],
    ('wxaccountmanage', 'GET'): ['admin'],
    ('wxaccountmanage', 'PUT'): ['admin'],
    ('wxaccountmanage', 'DELETE'): ['admin'],
    ('wxaccountmanage', 'POST'): ['admin'],
    ('apps_zabbix_status', 'GET'): ['user'],
    ('opsaccountmanage', 'GET'): ['admin'],
    ('opsaccountmanage', 'PUT'): ['admin'],
    ('opsaccountmanage', 'DELETE'): ['admin'],
    ('opsaccountmanage', 'POST'): ['admin'],
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):

    import six

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

