# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import current_app as app
import redis
from influxdb import InfluxDBClient


engine = create_engine('postgresql://postgres:cmdb@54.223.98.251:5432/cmdb', echo=True, pool_size=20, max_overflow=0, encoding='utf-8')
Base = declarative_base()
session = sessionmaker(bind=engine)
DBsession = session()

influxdb_client = InfluxDBClient(app.config['INFLUXDB_IP'], app.config['INFLUXDB_PORT'] , app.config['INFLUXDB_USER'], app.config['INFLUXDB_PASSWORD'], app.config['INFLUXDB_DATABASE'])
#influxdb_client = InfluxDBClient('54.223.98.251',8086 ,'cmdb','cmdb','cmdb')

pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], db=app.config['REDIS_DATABASE'], decode_responses=True)
redis_client = redis.Redis(connection_pool=pool)
