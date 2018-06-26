# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import s3_collect,S3_res_keys,S3_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger
import random
import string

def s3data_to_db():
    now = datetime.datetime.now()
    s3_data = s3_collect()
    if s3_data is None:
        logger.error("s3 aws api receive data is none")
        return False
    for item in s3_data:
        res = aws_model.DBsession.query(aws_model.S3).filter_by(name=item["Name"]).first()
        if not res:
            s3_ins = aws_model.S3(aws_create_time=item["CreationDate"],
                      name=item["Name"],
                      size=item["Size"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status = True
            )
            aws_model.DBsession.add(s3_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            s3_to_db = DataToDB(item, res, S3_res_keys, S3_db_keys, now, aws_model.S3, s3_data, "Name")
            s3_to_db.update()

    diff_s3 = update_status(aws_model.S3, s3_data, "Name", "name")

    if diff_s3:
        for item in diff_s3:
            res = aws_model.DBsession.query(aws_model.S3).filter_by(name=item).first()
            if res.data_status is True:
                randstr = "".join(random.sample(string.ascii_lowercase+string.ascii_letters, 5))
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "name", res.name+"_"+randstr)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True

