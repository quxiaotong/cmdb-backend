# -*- coding: utf-8 -*-
from cmdb.models import aws_model
from sqlalchemy import exc
from cmdb.core.logformat import logger


class DataToDB(object):

    def __init__(self, item_collect,  res_db, res_keys, db_keys, now_time, table, aws_server_data, collect_key):
        self.item_collect = item_collect
        self.res_db = res_db
        self.res_keys = res_keys
        self.db_keys = db_keys
        self.now_time = now_time
        self.table = table
        self.aws_server_data = aws_server_data
        self.collect_key = collect_key

    def update(self):
        for i1, i2 in zip(self.res_keys, self.db_keys):
            if self.item_collect[i1] != getattr(self.res_db,  i2):
                    setattr(self.res_db,  i2,  self.item_collect[i1])
        setattr(self.res_db, "data_update_time", self.now_time)
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            logger.exception("Exception Logged")
            aws_model.DBsession.rollback()

def update_status(table, aws_server_data, collect_key, table_key):
    collect_data = set([])
    db_data = set([])
    server_db = aws_model.DBsession.query(table).all()
    for instance in aws_server_data:
        collect_data.add(instance[collect_key])
    for instance in server_db:
        db_data.add(getattr(instance, table_key))
    diff_data = db_data-collect_data
    return diff_data








