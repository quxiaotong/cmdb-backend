# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import vol_collect,Vol_res_keys,Vol_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger

def voldata_to_db():
    now = datetime.datetime.now()
    vol_data = vol_collect()
    if vol_data is None:
        logger.error("volume aws api receive data is none")
        return False
    for item in vol_data:
        res = aws_model.DBsession.query(aws_model.Volume).filter_by(volume_id=item["VolumeId"]).first()
        if not res:
            ec2_obj = aws_model.DBsession.query(aws_model.Ec2).filter_by(instance_id=item["InstanceId"]).first()
            if not ec2_obj:
                ec2_instance_name = "None"
                ec2_instance_id = "None"
            else:
                ec2_instance_name = ec2_obj.name
                ec2_instance_id = ec2_obj.instance_id
            vol_ins = aws_model.Volume(volume_id=item["VolumeId"],
                       size=item["Size"],
                       state=item["State"],
                       aws_create_time=item["CreateTime"],
                       iops=item["Iops"],
                       device=item["Device"],
                       ec2_instance_name=ec2_instance_name,
                       ec2_instance_id=ec2_instance_id,
                       volume_type=item["VolumeType"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True
            )
            aws_model.DBsession.add(vol_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            vol_to_db = DataToDB(item, res, Vol_res_keys, Vol_db_keys, now, aws_model.Volume, vol_data, "VolumeId")
            vol_to_db.update()

    diff_rds = update_status(aws_model.Volume, vol_data, "VolumeId", "volume_id")

    if diff_rds:
        for item in diff_rds:
            res = aws_model.DBsession.query(aws_model.Volume).filter_by(volume_id=item).first()
            if res.data_status is True:
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True
