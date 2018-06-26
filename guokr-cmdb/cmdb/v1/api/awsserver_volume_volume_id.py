# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from ..errors import abort
from cmdb.models import aws_model

class AwsserverVolumeVolumeId(Resource):

    def put(self, volume_id):
        run_status = g.args.get("state")
        vol_instance = aws_model.DBsession.query(aws_model.Volume).filter(aws_model.Volume.volume_id == volume_id).first()
        if not vol_instance:
            abort('volume_not_found')
        aws_model.DBsession.query(aws_model.Volume).filter(aws_model.Volume.volume_id == volume_id).update({"state":run_status})
        aws_model.DBsession.commit()
        db_res_vol = aws_model.DBsession.query(aws_model.Volume).filter(aws_model.Volume.volume_id == volume_id).first()
        res = []
        res.append(db_res_vol)
        return res, 201, None

    def delete(self, volume_id):
        vol_instance = aws_model.DBsession.query(aws_model.Volume).filter(aws_model.Volume.volume_id == volume_id).first()
        if not vol_instance:
            abort('ec2_not_found')
        aws_model.DBsession.query(aws_model.Volume).filter(aws_model.Volume.volume_id == volume_id).update({"data_status":False})
        aws_model.DBsession.commit()
        return {"OK":True}, 201, None