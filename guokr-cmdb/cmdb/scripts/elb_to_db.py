# -*- coding: utf-8 -*-
from cmdb.core.aws_collection import elb_collect,Elb_res_keys,Elb_db_keys
from cmdb.scripts.base import DataToDB, update_status
from cmdb.models import aws_model
import datetime
from sqlalchemy import exc
from cmdb.core.logformat import logger
import random
import string

def elbdata_to_db():
    now = datetime.datetime.now()
    elb_data = elb_collect()
    if elb_data is None:
        logger.error("elb aws api receive data is none")
        return False
    for item in elb_data:
        res = aws_model.DBsession.query(aws_model.Elb).filter_by(dns_name=item["DNSName"]).first()
        vpc = aws_model.DBsession.query(aws_model.Vpc).filter_by(vpc_id=item["VPCId"]).first()
        if not res:
            ec2_list = []
            for ec2_ins in item["Instances"]:
                ec2_qurey = aws_model.DBsession.query(aws_model.Ec2).filter_by(instance_id=ec2_ins["InstanceId"]).first()
                ec2_list.append(ec2_qurey)
            elb_ins = aws_model.Elb(loadbalancer_name=item["LoadBalancerName"],
                       loadbalancer_port=item["LoadBalancerPort"],
                       instance_port=item["InstancePort"],
                       aws_create_time=item["CreatedTime"],
                       # vpc_id=vpc.id,
                       dns_name=item["DNSName"],
                       data_create_time=now,
                       data_update_time=now,
                       data_status=True,
                       ec2=ec2_list,
                    )
            aws_model.DBsession.add(elb_ins)
            try:
                aws_model.DBsession.commit()
            except exc.SQLAlchemyError:
                logger.exception("Exception Logged")
                aws_model.DBsession.rollback()
        else:
            elb_to_db = DataToDB(item, res, Elb_res_keys, Elb_db_keys, now, aws_model.Elb, elb_data, "DNSName")
            elb_to_db.update()

    diff_elb = update_status(aws_model.Elb, elb_data, "DNSName", "dns_name")

    if diff_elb:
        for item in diff_elb:
            res = aws_model.DBsession.query(aws_model.Elb).filter_by(dns_name=item).first()
            if res.data_status is True:
                randstr = "".join(random.sample(string.ascii_lowercase+string.ascii_letters, 5))
                setattr(res, "data_status", False)
                setattr(res, "data_update_time", now)
                setattr(res, "loadbalancer_name", res.loadbalancer_name+"_"+randstr)
                try:
                    aws_model.DBsession.commit()
                except exc.SQLAlchemyError:
                    logger.exception("Exception Logged")
                    aws_model.DBsession.rollback()
    return True
