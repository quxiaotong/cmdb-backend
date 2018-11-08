 # -*- coding: utf-8 -*-
from __future__ import absolute_import
from os import environ
from celery.schedules import crontab
from datetime import timedelta

class EnvConfigType(type):

    def __getattribute__(cls, key):
        value = object.__getattribute__(cls, key)
        env = environ.get(key)
        if env is not None:
            value = type(value)(env)
        return value


class Config(object):

    __metaclass__ = EnvConfigType

    DEBUG = True
    ERROR_404_HELP = False
    SECRET = "SofJ83pY7jmGsLgM"
    #SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        environ.get('MYSQL_USER', 'postgres'),
        environ.get('MYSQL_PASSWORD', 'cmdb'),
        environ.get('MYSQL_HOST', '54.223.98.251'),
        environ.get('MYSQL_PORT', '5432'),
        environ.get('MYSQL_DATABASE', 'cmdb'))
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #Server
    LISTEN = '0.0.0.0'
    LISTEN_ON = environ.get("LISTEN_ON",14500)

    #Redis
    REDIS_HOST = environ.get('REDIS_HOST', "'54.223.98.251'"),
    REDIS_PORT = environ.get('REDIS_PORT', '6379'),
    REDIS_DATABASE = environ.get('REDIS_DATABASE', '10'),


    #Celery
    CELERY_BROKER_URL = 'redis://%s:%s' % (
        environ.get('REDIS_HOST', '10.10.0.212'), #ansible
        environ.get('REDIS_PORT', '6379'))
    CELERY_RESULT_BACKEND = 'redis://%s:%s' % (
        environ.get('REDIS_HOST', '10.10.0.212'),
        environ.get('REDIS_PORT', '6379'))
    CELERY_TIMEZONE = 'Asia/Shanghai'
    # CELERYD_LOG_FILE = '/tmp/celery.log'
    CELERYD_LOG_FILE = 'celery.log'
    CELERY_ENABLE_BEAT = True
    PG_PERIOD = environ.get('PG_PERIOD', '600')
    IF_PERIOD = environ.get('IF_PERIOD', '3700')
    APP_PERIOD = environ.get('APP_PERIOD', '300')
    ETCD_PERIOD = environ.get('ETCD_PERIOD', '60')
    CELERYBEAT_SCHEDULE = {
         # Executes every  morning at 4:00 A.M
        # 'alldata_to_db': {
        #     'task': 'cmdb.scripts.alldata_to_db.alldata_to_db',
        #     'schedule': crontab(minute=0, hour=4),
        #  },
        'data_to_db': {
            'task': 'cmdb.core.task.alldata_to_db.data_to_db',
            'schedule': timedelta(seconds=int(PG_PERIOD)),
        },
        'all_cloudwatch_to_influx': {
            'task': 'cmdb.core.task.cloudwatch_to_influx.cloudwatch',
            'schedule': timedelta(seconds=int(IF_PERIOD)),
        },
        'serivce_etcd_to_db': {
            'task': 'cmdb.core.task.etcd_to_db.etcdtodb',
            'schedule': timedelta(seconds=int(ETCD_PERIOD)),
        },
        # 'app_to_influx': {
        #     'task': 'cmdb.core.task.ansible_tasks_to_db.app_to_influx',
        #     'schedule': timedelta(seconds=int(APP_PERIOD)),
        # },
    }

    #mail
    MAIL_SENDER = '18518691662@163.com'
    MAIL_PASSWORD = 'qxt596790029'
    MAIL_RECEIVER = 'xiaotong.qu@guokr.com'

    #INFLUXDB
    INFLUXDB_IP = environ.get('INFLUXDB', '54.223.98.251')
    INFLUXDB_PORT = environ.get('PORT', '8086')
    INFLUXDB_USER = environ.get('NAME', 'cmdb')
    INFLUXDB_PASSWORD = environ.get('PASSWORD', 'cmdb')
    INFLUXDB_DATABASE = environ.get('DATABASE', 'cmdb')

    #ANSIBLE_HOSTS
    ANSIBLE_HOSTS = environ.get("ANSIBLE_HOSTS", "/tmp/ansible_hosts")

    #ZABBIX_URL
    ZABBIX_URL = 'http://zabbix.guokr.com'
    ZABBIX_USER = 'admin'
    ZABBIX_PASSWORD = 'zabbix'

    #ETCD
    ETCD = environ.get('INFLUXDB', '54.223.98.251')
    ETCD_PORT = environ.get('ETCD_PORT', 2379)

    #ElasticAPM
    APM_ENABLE = True
    APM_SERVICE_NAME = 'cmdb'
    APM_SERVICE_TOKEN = ''
    APM_SERVER_URL = 'http://180.76.150.178:8200'
    APM_DEBUG = True