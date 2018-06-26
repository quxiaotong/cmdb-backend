# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
from cmdb.core.logformat import logger
from cmdb.core.task.celery_base import celery


@celery.task()
def data_to_db():
    from cmdb.models import aws_model
    from cmdb.scripts.ec_to_db import ecdata_to_db
    from cmdb.scripts.rds_to_db import rdsdata_to_db
    from cmdb.scripts.elb_to_db import elbdata_to_db
    from cmdb.scripts.vpc_to_db import vpcdata_to_db
    from cmdb.scripts.s3_to_db import s3data_to_db
    from cmdb.scripts.iam_to_db import iamdata_to_db
    from cmdb.scripts.vol_to_db import voldata_to_db
    from cmdb.scripts.ec2_to_db import ec2data_to_db
    now = datetime.datetime.now()
    res_iam = iamdata_to_db()
    if res_iam is False:
        logger.error("iam data to db is Failed ")
        log_data=aws_model.LogCrontab(content="iam table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data=aws_model.LogCrontab(content="iam table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_s3 = s3data_to_db()
    if res_s3 is False:
        logger.error("s3 data to db is Failed ")
        log_data=aws_model.LogCrontab(content="s3 table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data=aws_model.LogCrontab(content="s3 table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_ec = ecdata_to_db()
    if res_ec is False:
        logger.error("ec data to db is Failed ")
        log_data=aws_model.LogCrontab(content="ec table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data=aws_model.LogCrontab(content="ec table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_vpc = vpcdata_to_db()
    if res_vpc == False:
        logger.error("vpc data to db is Failed ")
        log_data=aws_model.LogCrontab(content="vpc table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data=aws_model.LogCrontab(content="vpc table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_elb = elbdata_to_db()
    if res_elb == False:
        logger.error("elb data to db is Failed ")
        log_data=aws_model.LogCrontab(content="elb table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data=aws_model.LogCrontab(content="elb table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_ec2 = ec2data_to_db()
    if res_ec2 is False:
        logger.error("ec2 data to db is Failed ")
        log_data = aws_model.LogCrontab(content="ec2 table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data = aws_model.LogCrontab(content="ec2 table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_rds = rdsdata_to_db()
    if res_rds is False:
        logger.error("rds data to db is Failed ")
        log_data = aws_model.LogCrontab(content="rds table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data = aws_model.LogCrontab(content="rds table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

    res_vol = voldata_to_db()
    if res_vol is False:
        logger.error("volume data to db is Failed ")
        log_data = aws_model.LogCrontab(content="volume table update failed", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()
    else:
        log_data = aws_model.LogCrontab(content="volume table update successfully", data_create_time=now)
        aws_model.DBsession.add(log_data)
        aws_model.DBsession.commit()

