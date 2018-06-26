# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import ec_collect,Ec_res_keys,Ec_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger
import random
import string

def ecdata_to_db():
    now = datetime.datetime.now()
    ec_data = ec_collect()
    if ec_data is None:
        logger.error("elasticache aws api receive data is none")
        return False
    for item in ec_data:
        res = aws_model.DBsession.query(aws_model.Elasticache).filter_by(cachecluster_id=item["CacheClusterId"]).first()
        if not res:
            ec_type_query = aws_model.DBsession.query(aws_model.Ectype)
            ec_type_query = ec_type_query.filter_by(type=item["CacheNodeType"])
            ec_type_obj = ec_type_query.first()
            if not ec_type_obj:
                logger.error("Ectype table don't have the elasticache_type of %s" %item["InstanceType"])
                log_data=aws_model.LogCrontab(content="new instance %s of Elasticache don't have the Elasticache_type of %s"
                                                     %(item["CacheClusterId"], item["InstanceType"]), data_create_time=now)
                aws_model.DBsession.add(log_data)
                aws_model.DBsession.commit()
                continue
            ec_ins = aws_model.Elasticache(cachecluster_id=item["CacheClusterId"],
                               aws_create_time=item["CacheClusterCreateTime"],
                               status=item["CacheClusterStatus"],
                               engine=item["Engine"],
                               cachenode_type=ec_type_obj.type,
                               data_create_time=now,
                               data_update_time=now,
                               data_status=True
            )
            aws_model.DBsession.add(ec_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            ec_to_db = DataToDB(item, res, Ec_res_keys, Ec_db_keys, now, aws_model.Elasticache, ec_data, "CacheClusterId")
            ec_to_db.update()

    diff_ec = update_status(aws_model.Elasticache, ec_data, "CacheClusterId", "cachecluster_id")

    if diff_ec:
        for item in diff_ec:
            res = aws_model.DBsession.query(aws_model.Elasticache).filter_by(cachecluster_id=item).first()
            if res.data_status is True:
                randstr = "".join(random.sample(string.ascii_lowercase+string.ascii_letters, 5))
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "cachecluster_id", res.cachecluster_id+"_"+randstr)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True
