# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/v1'


DefinitionsElasticache = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'cachenode_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'memory_num': {'type': 'integer'}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'status': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'engine': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'cachecluster_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsToken = {'type': 'array', 'items': {'properties': {'access_token': {'type': 'string'}}}}
DefinitionsIam = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'create_date': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'user_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'password_lastused': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'user_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsSysconfig = {'type': 'array', 'items': {'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'value': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'user_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsVpc = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'status': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'vpc_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'cidrblock': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsCloudwatch_test = {'type': 'list'}
DefinitionsOpsaccount = {'type': 'array', 'items': {'properties': {'id': {'type': 'integer'}, 'mark': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'platform': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'secret': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'account': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsApps = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'listen_port': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'name': {'type': 'string', 'minLength': 1, 'maxLength': 6}, 'utilization': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'memory': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'cpu': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'host_ip': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsProjname = {'type': 'array', 'items': {'properties': {'name': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsElb = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'vpc_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'dns_name': {'type': 'string', 'minLength': 1, 'maxLength': 128}, 'loadbalancer_port': {'type': 'integer'}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'instance_port': {'type': 'integer'}, 'id': {'type': 'integer'}, 'loadbalancer_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsOpsconfigmanage_data = {'required': ['account', 'secret'], 'properties': {'account': {'type': 'string'}, 'platform': {'type': 'string'}, 'mark': {'type': 'string'}, 'secret': {'type': 'string'}}}
DefinitionsCloudwatch = {'type': 'array', 'items': {'properties': {'CPUUtilization': {'type': 'float'}, 'NetworkIn': {'type': 'float'}, 'HTTPCode_Backend_5XX': {'type': 'float'}, 'time': {'type': 'string'}, 'RequestCount': {'type': 'float'}, 'FreeableMemory': {'type': 'float'}, 'SwapUsage': {'type': 'float'}, 'DatabaseConnections': {'type': 'float'}}}}
DefinitionsDisk = {'type': 'array', 'items': {'properties': {'mount_dir': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'all_size': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'avail_size': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'used_size': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'device': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'used_percent': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsRds = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'cpu_num': {'type': 'integer'}, 'db_identifier': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'memory_num': {'type': 'integer'}, 'status': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'storage_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'engine': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'resource_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'instance_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsVolume = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'volume_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'ec2_instance_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'state': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'size': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'volume_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'ec2_instance_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'device': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'iops': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsEc2 = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'cpu_num': {'type': 'integer'}, 'keyname': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'utilization': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'memory_num': {'type': 'integer'}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'public_ip': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'private_ip': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'instance_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'run_state': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'vpc_id': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'instance_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsCmdbaccount = {'required': ['account', 'secret'], 'properties': {'authority': {'type': 'string', 'description': '用户权限身份', 'enum': ['admin', 'user']}, 'secret': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'account': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'make_secret': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}
DefinitionsSysconfigmanage_data = {'required': ['app_name', 'key', 'value', 'user_name'], 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'value': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'user_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'app_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}
DefinitionsS3 = {'type': 'array', 'items': {'properties': {'aws_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_status': {'type': 'boolean', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'aws_creation_date': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'size': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsCmdb_user_get = {'type': 'array', 'items': {'properties': {'authority': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'account': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsSuccess = {'properties': {'ok': {'type': 'boolean'}}}
DefinitionsWxaccount = {'type': 'array', 'items': {'required': ['use_type', 'name', 'type', 'mail', 'secret', 'use_name', 'phone'], 'properties': {'use_name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'phone': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_update_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'data_create_time': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'type': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'mail': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'id': {'type': 'integer'}, 'use_type': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'name': {'type': 'string', 'minLength': 1, 'maxLength': 64}, 'secret': {'type': 'string', 'minLength': 1, 'maxLength': 64}}}}
DefinitionsError = {'properties': {'error_code': {'type': 'string'}, 'text': {'type': 'string'}, 'message': {'type': 'string'}}}

validators = {
    ('cloudwatch_rds_instance_identifier', 'GET'): {'args': {'required': ['rds_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'rds_monitor_item': {'type': 'string', 'description': '监控项', 'enum': ['FreeableMemory', 'FreeStorageSpace', 'ReadIOPS', 'ReadLatency', 'NetworkReceiveThroughput', 'NetworkTransmitThroughput', 'SwapUsage', 'WriteIOPS', 'WriteLatency', 'DatabaseConnections']}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}}}},
    ('awsserver_ec2_instance_ip_point_status', 'GET'): {'args': {'required': ['monitor_item'], 'properties': {'monitor_item': {'type': 'string', 'description': 'app的监控项', 'enum': ['cpu', 'memery']}, 'time_point': {'type': 'string', 'required': False, 'description': 'app运行状态的时间点'}}}},
    ('awsserver_rds_rds_instance_identifier', 'PUT'): {'args': {'required': ['status'], 'properties': {'status': {'type': 'string'}}}},
    ('apps_apphost_point_status', 'GET'): {'args': {'required': ['host_ip', 'monitor_item'], 'properties': {'monitor_item': {'type': 'string', 'description': 'app的监控项', 'enum': ['cpu', 'memery']}, 'host_ip': {'type': 'string', 'description': 'app运行的服务器ip'}, 'time_point': {'required': False, 'type': 'string', 'description': 'app运行状态的时间点'}}}},
    ('cmdbaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('cmdbaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'opsaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('cmdbaccountmanage', 'PUT'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('apps_app_id_status', 'GET'): {'args': {'required': ['app_name', 'sys_status', 'end_time', 'polymerization', 'period'], 'properties': {'app_name': {'type': 'string', 'description': '业务线名字'}, 'sys_status': {'type': 'string', 'description': '监控项', 'enum': ['cpu', 'memery']}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}}}},
    ('sysconfigmanage', 'POST'): {'form': {'required': [], 'properties': {'config_data': {'schema': DefinitionsSysconfigmanage_data}}}},
    ('sysconfigmanage', 'GET'): {'args': {'required': ['app_name'], 'properties': {'app_name': {'type': 'string'}}}},
    ('sysconfigmanage', 'DELETE'): {'form': {'required': [], 'properties': {'sysaccountmanage_id': {'schema': {'required': ['sysconfig_id'], 'sysconfig_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('sysconfigmanage', 'PUT'): {'form': {'required': [], 'properties': {'config_data': {'schema': DefinitionsSysconfigmanage_data}}}},
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): {'args': {'required': ['elasticache_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'elasticache_monitor_item': {'type': 'string', 'description': '监控项', 'enum': ['BytesUsedForCache', 'CacheHits', 'CacheMisses', 'CPUUtilization', 'CurrConnections', 'CurrItems', 'FreeableMemory', 'Reclaimed', 'NetworkBytesIn']}, 'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}}}},
    ('cloudwatch_ec2_instance_id', 'GET'): {'args': {'required': ['ec2_monitor_item', 'end_time', 'polymerization', 'period'], 'properties': {'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'ec2_monitor_item': {'type': 'string', 'description': '监控项', 'enum': ['CPUUtilization', 'DiskReadBytes', 'DiskReadOps', 'DiskWriteBytes', 'DiskWriteOps', 'NetworkIn', 'NetworkOut']}}}},
    ('cloudwatch_elb_loadbalancer_name', 'GET'): {'args': {'required': ['elb_monitor_item', 'start_time', 'end_time', 'period', 'polymerization'], 'properties': {'start_time': {'type': 'string', 'description': '获得监控数据的起始时间'}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'elb_monitor_item': {'type': 'string', 'description': '监控项', 'enum': ['UnHealthyHostCount', 'RequestCount', 'Latency', 'HealthyHostCount', 'BackendConnectionErrors', 'HTTPCode_Backend_5XX', 'HTTPCode_ELB_5XX', 'HTTPCode_Backend_4XX']}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}, 'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}}}},
    ('awsserver_elasticache_cachecluster_id', 'PUT'): {'args': {'required': ['status'], 'properties': {'status': {'type': 'string'}}}},
    ('awsserver_volume_volume_id', 'PUT'): {'args': {'required': ['state'], 'properties': {'state': {'type': 'string'}}}},
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): {'args': {'required': ['end_time', 'polymerization', 'period'], 'properties': {'polymerization': {'type': 'string', 'description': '数据的聚合函数', 'enum': ['Average', 'Minimum', 'Maximum']}, 'period': {'type': 'string', 'description': '每隔多长时间获得一次数据'}, 'end_time': {'type': 'string', 'description': '获得监控数据的结束时间'}}}},
    ('awsserver_ec2', 'GET'): {'args': {'required': [], 'properties': {'页数': {'type': 'string', 'default': 20, 'description': '显示列表分页数', 'required': False}, '每页的行数': {'type': 'string', 'default': 1, 'description': '显示每页行数', 'required': False}}}},
    ('wxaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'wxconfig_data': {'schema': DefinitionsWxaccount}}}},
    ('wxaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'wxaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('wxaccountmanage', 'PUT'): {'form': {'required': ['account_id'], 'properties': {'account_id': {'type': 'string'}, 'wxconfig_data': {'schema': DefinitionsWxaccount}}}},
    ('opsaccountmanage', 'POST'): {'form': {'required': [], 'properties': {'config_data': {'schema': DefinitionsOpsconfigmanage_data}}}},
    ('opsaccountmanage', 'DELETE'): {'form': {'required': [], 'properties': {'opsaccountmanage_id': {'schema': {'required': ['account_id'], 'account_id': {'type': 'string'}}, 'description': '配置管理资源的id'}}}},
    ('opsaccountmanage', 'PUT'): {'form': {'required': ['account_id'], 'properties': {'config_data': {'schema': DefinitionsOpsconfigmanage_data}, 'account_id': {'type': 'string'}}}},
    ('login', 'POST'): {'form': {'required': [], 'properties': {'cmdbaccount': {'schema': DefinitionsCmdbaccount}}}},
    ('apps_app_name_zabbix', 'GET'): {'args': {'required': [], 'properties': {'time_point': {'type': 'string', 'required': False, 'description': 'app运行状态的时间点'}, 'zab_app_webitem': {'required': False, 'type': 'string', 'description': 'zabbix应用app的监控项'}}}},
}

filters = {
    ('cloudwatch_rds_instance_identifier', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_ec2_instance_ip_point_status', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_rds_rds_instance_identifier', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('awsserver_rds_rds_instance_identifier', 'PUT'): {201: {'schema': DefinitionsRds, 'headers': None}},
    ('awsserver_vpc', 'GET'): {200: {'schema': DefinitionsVpc, 'headers': None}},
    ('apps_apphost_point_status', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('cmdbaccountmanage', 'POST'): {200: {'schema': DefinitionsCmdb_user_get, 'headers': None}},
    ('cmdbaccountmanage', 'GET'): {200: {'schema': DefinitionsCmdb_user_get, 'headers': None}},
    ('cmdbaccountmanage', 'DELETE'): {200: {'schema': DefinitionsCmdb_user_get, 'headers': None}},
    ('cmdbaccountmanage', 'PUT'): {200: {'schema': DefinitionsCmdb_user_get, 'headers': None}},
    ('apps_app_id_status', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_ec2_instance_ip_disk', 'GET'): {200: {'schema': DefinitionsDisk, 'headers': None}},
    ('sysconfigmanage', 'POST'): {200: {'schema': DefinitionsSysconfig, 'headers': None}},
    ('sysconfigmanage', 'GET'): {200: {'schema': DefinitionsSysconfig, 'headers': None}},
    ('sysconfigmanage', 'DELETE'): {200: {'schema': DefinitionsSysconfig, 'headers': None}},
    ('sysconfigmanage', 'PUT'): {200: {'schema': DefinitionsSysconfig, 'headers': None}},
    ('awsserver_s3_s3_name', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('active', 'GET'): {200: {'schema': None, 'headers': None}},
    ('awsserver_rds', 'GET'): {200: {'schema': DefinitionsRds, 'headers': None}},
    ('apps_proj_name_app_id', 'GET'): {200: {'schema': DefinitionsApps, 'headers': None}},
    ('cloudwatch_ec2_instance_id', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_elb', 'GET'): {200: {'schema': DefinitionsElb, 'headers': None}},
    ('awsserver_elasticache', 'GET'): {200: {'schema': DefinitionsElasticache, 'headers': None}},
    ('awsserver_ec2_instance_ip', 'GET'): {200: {'schema': DefinitionsEc2, 'headers': None}},
    ('cloudwatch_elb_loadbalancer_name', 'GET'): {200: {'schema': DefinitionsCloudwatch, 'headers': None}},
    ('awsserver_s3', 'GET'): {200: {'schema': DefinitionsS3, 'headers': None}},
    ('awsserver_iam', 'GET'): {200: {'schema': DefinitionsIam, 'headers': None}},
    ('awsserver_elasticache_cachecluster_id', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('awsserver_elasticache_cachecluster_id', 'PUT'): {201: {'schema': DefinitionsElasticache, 'headers': None}},
    ('awsserver_volume_volume_id', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('awsserver_volume_volume_id', 'PUT'): {201: {'schema': DefinitionsVolume, 'headers': None}},
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_ec2', 'GET'): {200: {'schema': DefinitionsEc2, 'headers': None}},
    ('wxaccountmanage', 'POST'): {200: {'schema': DefinitionsWxaccount, 'headers': None}},
    ('wxaccountmanage', 'GET'): {200: {'schema': DefinitionsWxaccount, 'headers': None}},
    ('wxaccountmanage', 'DELETE'): {200: {'schema': DefinitionsWxaccount, 'headers': None}},
    ('wxaccountmanage', 'PUT'): {200: {'schema': DefinitionsWxaccount, 'headers': None}},
    ('awsserver_iam_user_id', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('awsserver_elb_loadbalancer_name', 'DELETE'): {201: {'schema': DefinitionsSuccess, 'headers': None}},
    ('apps_proj_name', 'GET'): {200: {'schema': DefinitionsProjname, 'headers': None}},
    ('apps_zabbix_status', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
    ('awsserver_volume', 'GET'): {200: {'schema': DefinitionsVolume, 'headers': None}},
    ('opsaccountmanage', 'POST'): {200: {'schema': DefinitionsOpsaccount, 'headers': None}},
    ('opsaccountmanage', 'GET'): {200: {'schema': DefinitionsOpsaccount, 'headers': None}},
    ('opsaccountmanage', 'DELETE'): {200: {'schema': DefinitionsOpsaccount, 'headers': None}},
    ('opsaccountmanage', 'PUT'): {200: {'schema': DefinitionsOpsaccount, 'headers': None}},
    ('login', 'POST'): {200: {'schema': DefinitionsToken, 'headers': None}},
    ('apps_app_name_zabbix', 'GET'): {200: {'schema': DefinitionsCloudwatch_test, 'headers': None}},
}

scopes = {
    ('cloudwatch_rds_instance_identifier', 'GET'): ['user'],
    ('awsserver_ec2_instance_ip_point_status', 'GET'): ['user'],
    ('awsserver_rds_rds_instance_identifier', 'DELETE'): ['admin'],
    ('awsserver_rds_rds_instance_identifier', 'PUT'): ['user'],
    ('awsserver_vpc', 'GET'): ['user'],
    ('apps_apphost_point_status', 'GET'): ['user'],
    ('cmdbaccountmanage', 'POST'): ['admin'],
    ('cmdbaccountmanage', 'GET'): ['admin'],
    ('cmdbaccountmanage', 'DELETE'): ['admin'],
    ('cmdbaccountmanage', 'PUT'): ['admin'],
    ('apps_app_id_status', 'GET'): ['user'],
    ('awsserver_ec2_instance_ip_disk', 'GET'): ['user'],
    ('sysconfigmanage', 'POST'): ['admin'],
    ('sysconfigmanage', 'GET'): ['admin'],
    ('sysconfigmanage', 'DELETE'): ['admin'],
    ('sysconfigmanage', 'PUT'): ['admin'],
    ('awsserver_s3_s3_name', 'DELETE'): ['admin'],
    ('cloudwatch_elasticache_cachecluster_id', 'GET'): ['user'],
    ('awsserver_rds', 'GET'): ['user'],
    ('apps_proj_name_app_id', 'GET'): ['user'],
    ('cloudwatch_ec2_instance_id', 'GET'): ['user'],
    ('awsserver_elb', 'GET'): ['user'],
    ('awsserver_elasticache', 'GET'): ['user'],
    ('awsserver_ec2_instance_ip', 'GET'): ['user'],
    ('cloudwatch_elb_loadbalancer_name', 'GET'): ['user'],
    ('awsserver_s3', 'GET'): ['user'],
    ('awsserver_iam', 'GET'): ['user'],
    ('awsserver_elasticache_cachecluster_id', 'DELETE'): ['admin'],
    ('awsserver_elasticache_cachecluster_id', 'PUT'): ['user'],
    ('awsserver_volume_volume_id', 'DELETE'): ['user'],
    ('awsserver_volume_volume_id', 'PUT'): ['admin'],
    ('awsserver_ec2_instance_ip_monitor_item', 'GET'): ['user'],
    ('awsserver_ec2', 'GET'): ['user'],
    ('wxaccountmanage', 'POST'): ['admin'],
    ('wxaccountmanage', 'GET'): ['admin'],
    ('wxaccountmanage', 'DELETE'): ['admin'],
    ('wxaccountmanage', 'PUT'): ['admin'],
    ('awsserver_iam_user_id', 'DELETE'): ['admin'],
    ('awsserver_elb_loadbalancer_name', 'DELETE'): ['admin'],
    ('apps_proj_name', 'GET'): ['user'],
    ('apps_zabbix_status', 'GET'): ['user'],
    ('awsserver_volume', 'GET'): ['user'],
    ('opsaccountmanage', 'POST'): ['admin'],
    ('opsaccountmanage', 'GET'): ['admin'],
    ('opsaccountmanage', 'DELETE'): ['admin'],
    ('opsaccountmanage', 'PUT'): ['admin'],
    ('apps_app_name_zabbix', 'GET'): ['user'],
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

