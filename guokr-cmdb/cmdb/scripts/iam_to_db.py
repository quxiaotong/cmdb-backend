# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import iam_collect, Iam_res_keys, Iam_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
from datetime import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger
import random
import string

def iamdata_to_db():
    now = datetime.now()
    iam_data = iam_collect()
    if iam_data is None:
        logger.error("iam aws api receive data is none")
        return False
    for item in iam_data:
        res = aws_model.DBsession.query(aws_model.Iam).filter_by(user_id=item["UserId"]).first()
        if not res:
            iam_ins = aws_model.Iam(user_id=item["UserId"],
                       user_name=item["UserName"],
                       password_lastused=item["PasswordLastUsed"],
                       aws_create_time=item["CreateDate"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True
             )
            aws_model.DBsession.add(iam_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            iam_to_db = DataToDB(item, res, Iam_res_keys, Iam_db_keys, now, aws_model.Iam, iam_data, "UserId")
            iam_to_db.update()

    diff_iam = update_status(aws_model.Iam, iam_data, "UserId", "user_id")

    if diff_iam:
        for item in diff_iam:
            res = aws_model.DBsession.query(aws_model.Iam).filter_by(user_id=item).first()
            if res.data_status is True:
                randstr = "".join(random.sample(string.ascii_lowercase+string.ascii_letters, 5))
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "user_name", res.user_name+"_"+randstr)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True
