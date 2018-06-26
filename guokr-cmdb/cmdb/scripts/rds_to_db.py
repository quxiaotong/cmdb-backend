# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import rds_collect,Rds_res_keys,Rds_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger
import random
import string

def rdsdata_to_db():
    now = datetime.datetime.now()
    rds_data = rds_collect()
    if rds_data is None:
        logger.error("rds aws api receive data is none")
        return False
    for item in rds_data:
        res = aws_model.DBsession.query(aws_model.Rds).filter_by(resource_id=item["DbiResourceId"]).first()
        if not res:
            rds_type_query = aws_model.DBsession.query(aws_model.Rdstype)
            rds_type_query = rds_type_query.filter_by(type=item["DBInstanceClass"])
            rds_type_obj = rds_type_query.first()
            vpc = aws_model.DBsession.query(aws_model.Vpc).filter_by(vpc_id=item["VpcId"]).first()
            if not rds_type_obj:
                logger.error("Ectype table don't have the elasticache_type of %s" %item["InstanceType"])
                log_data=aws_model.LogCrontab(content="new instance %s of rds don't have the rds_type of %s"
                                                     %(item["DBInstanceIdentifier"], item["InstanceType"]), data_create_time=now)
                aws_model.DBsession.add(log_data)
                aws_model.DBsession.commit()
                continue
            rds_ins = aws_model.Rds(db_identifier=item["DBInstanceIdentifier"],
                       status=item["DBInstanceStatus"],
                       engine = item["Engine"],
                       resource_id=item["DbiResourceId"],
                       aws_create_time=item["InstanceCreateTime"],
                       instance_type=rds_type_obj.type,
                       vpc_id=vpc.id,
                       storage_type=item["StorageType"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True
            )
            aws_model.DBsession.add(rds_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            rds_to_db = DataToDB(item, res, Rds_res_keys, Rds_db_keys, now, aws_model.Rds, rds_data, "DbiResourceId")
            rds_to_db.update()

    diff_rds = update_status(aws_model.Rds, rds_data, "DbiResourceId", "resource_id")

    if diff_rds:
        for item in diff_rds:
            res = aws_model.DBsession.query(aws_model.Rds).filter_by(resource_id=item).first()
            if res.data_status is True:
                randstr = "".join(random.sample(string.ascii_lowercase+string.ascii_letters,5))
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "db_identifier", res.db_identifier+"_"+randstr)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True

