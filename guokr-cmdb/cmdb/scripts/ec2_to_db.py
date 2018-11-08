# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import exc
from cmdb.core.aws_collection import ec2_collect, Ec2_res_keys, Ec2_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
from cmdb.core.logformat import logger
from cmdb.core.mail import mail
from cmdb.core.ec2_utilization import ec2_utilizat


def ec2data_to_db():
    now = datetime.datetime.now()
    ec2_data = ec2_collect()
    aws_add_ec2 = []
    if ec2_data is None:
        logger.error("ec2 aws api receive data is none")
        return False
    for item in ec2_data:
        res = aws_model.DBsession.query(aws_model.Ec2).filter_by(instance_id=item["InstanceId"]).first()
        if not res:
            ec2_type_query = aws_model.DBsession.query(aws_model.Ec2type)
            ec2_type_query = ec2_type_query.filter_by(type=item["InstanceType"])
            ec2_type_obj = ec2_type_query.first()
            vpc = aws_model.DBsession.query(aws_model.Vpc).filter_by(vpc_id=item["VpcId"]).first()
            if not ec2_type_obj:
                logger.error("Ec2type table don't have the ec2_type of %s" %item["InstanceType"])
                log_data = aws_model.LogCrontab(content="new instance %s of ec2 don't have the ec2_type of %s"
                                                     %(item["Name"], item["InstanceType"]),data_create_time=now)
                aws_model.DBsession.add(log_data)
                aws_model.DBsession.commit()
                continue
            ec2_ins = aws_model.Ec2(instance_id=item["InstanceId"],
                       private_ip=item["PrivateIpAddress"],
                       public_ip=item["PublicIpAddress"],
                       run_state=item["State"],
                       keyname=item["KeyName"],
                       aws_create_time=item["LaunchTime"],
                       vpc_id=vpc.id,
                       name=item.get("Name"),
                       instance_type=ec2_type_obj.type,
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True
                           )
            aws_add_ec2.append(item["PrivateIpAddress"])
            aws_model.DBsession.add(ec2_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        elif item["State"] == "terminated":
            setattr(res, "data_update_time", now)
            setattr(res, "run_state", "terminated")
            setattr(res, "data_status", False)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            ec2_to_db = DataToDB(item, res, Ec2_res_keys, Ec2_db_keys, now, aws_model.Ec2, ec2_data, "InstanceId")
            ec2_to_db.update()

    #邮件通知新增的ec2实例
    aws_add_ec2 = " ".join(aws_add_ec2)
    if aws_add_ec2:
        res = mail(aws_add_ec2, "aws增加ec2,对比ansible的host文件去确认增加")
        if res is False:
            log_data = aws_model.LogCrontab(content="add ec2 send mail failed",data_create_time=now)
            aws_model.DBsession.add(log_data)
            aws_model.DBsession.commit()

    #逻辑删除释放的ec2并发邮件通知
    diff_ec2 = update_status(aws_model.Ec2, ec2_data, "InstanceId", "instance_id")
    if diff_ec2:
        aws_delete_ec2 = []
        for item in diff_ec2:
            res = aws_model.DBsession.query(aws_model.Ec2).filter_by(instance_id=item).first()
            if res.data_status is True:
                aws_delete_ec2.append(res.private_ip)
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
        aws_delete_ec2 = " ".join(aws_delete_ec2)
        if aws_delete_ec2:
            res = mail(aws_delete_ec2, "aws删除的ec2,对比ansible的host文件去确认删除")
            if res is False:
                log_data = aws_model.LogCrontab(content="delete ec2 send mail failed", data_create_time=now)
                aws_model.DBsession.add(log_data)
                aws_model.DBsession.commit()

    #容量计算
    ec2_all = aws_model.DBsession.query(aws_model.Ec2).filter(aws_model.Ec2.data_status == True).all()
    for ec2 in ec2_all:
        utilization = ec2_utilizat(ec2.instance_id)
        ec2.utilization = utilization
        try:
            aws_model.DBsession.commit()
        except exc.SQLAlchemyError:
            logger.exception("Exception Logged")
            aws_model.DBsession.rollback()

    return True
