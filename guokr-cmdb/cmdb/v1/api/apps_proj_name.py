# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from cmdb.models import aws_model

class AppsProjName(Resource):

    def get(self, proj_name):
        apps_name = aws_model.DBsession.query(aws_model.App.name).filter_by(project=proj_name).all()
        return apps_name, 200, None