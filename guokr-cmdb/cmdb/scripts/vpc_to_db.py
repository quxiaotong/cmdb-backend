# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import vpc_collect,Vpc_res_keys,Vpc_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger

def vpcdata_to_db():
    now = datetime.datetime.now()
    vpc_data = vpc_collect()
    if vpc_data is None:
        logger.error("vpc aws api receive data is none")
        return False
    for item in vpc_data:
        res = aws_model.DBsession.query(aws_model.Vpc).filter_by(vpc_id=item["VpcId"]).first()
        if not res:
            vpc_ins = aws_model.Vpc(vpc_id=item["VpcId"],
                       cidrblock=item["CidrBlock"],
                       status=item["State"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True
            )
            aws_model.DBsession.add(vpc_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            vpc_to_db = DataToDB(item, res, Vpc_res_keys, Vpc_db_keys, now, aws_model.Vpc, vpc_data, "VpcId")
            vpc_to_db.update()

    diff_vpc = update_status(aws_model.Vpc, vpc_data, "VpcId", "vpc_id")

    if diff_vpc:
        for item in diff_vpc:
            res = aws_model.DBsession.query(aws_model.Vpc).filter_by(vpc_id=item).first()
            if res.data_status is True:
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "status", "delete")
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True
