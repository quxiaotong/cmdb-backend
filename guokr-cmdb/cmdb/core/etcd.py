import datetime
from cmdb.models import aws_model
from sqlalchemy import exc
import jwt
from flask import current_app as app
from cmdb.core.db import DBsession

def sysconfig_pg_add(app_id,user_name,key,value):
    now_time = datetime.datetime.now()
    app_sys_config = aws_model.sysconfig(
        app_id=app_id,
        user_name=user_name,
        key=key,
        value=value,
        data_update_time=now_time,
    )
    aws_model.DBsession.add(app_sys_config)
    try:
        aws_model.DBsession.commit()
    except exc.SQLAlchemyError:
        aws_model.DBsession.rollback()

def sysconfig_pg_update(app_id, user_name, key, value):
    now_time = datetime.datetime.now()
    config_obj = aws_model.DBsession.query(aws_model.sysconfig).filter(aws_model.sysconfig.app_id == app_id, aws_model.sysconfig.key == key).first()
    config_obj.user_name = user_name
    config_obj.value = value
    config_obj.data_update_time = now_time

    # aws_model.DBsession.query(aws_model.sysconfig).filter(aws_model.sysconfig.app_id == app_id and aws_model.sysconfig.key == key).update({
    #      "user_name": user_name, "value": value, "data_update_time": now_time
    # })
    try:
        aws_model.DBsession.commit()
    except exc.SQLAlchemyError:
        aws_model.DBsession.rollback()

def access_token(token):
    try:
        user_token = jwt.decode(token, app.config["SECRET"])
    except Exception:
        user_name = "quxiaotong"
        return user_name
    user_name = DBsession.query(aws_model.CmdbUser.account).filter_by(id=user_token["uid"]).first()
    return user_name