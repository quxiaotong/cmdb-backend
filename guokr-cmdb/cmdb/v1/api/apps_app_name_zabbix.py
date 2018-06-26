# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
from datetime import datetime
import time
import re
from cmdb.core.zabbix_web import zab_web_itemids, zab_web_item_data
import json

class AppsAppNameZabbix(Resource):

    def get(self, app_name):

        end_time = g.args.get("time_point")
        item_name = g.args.get("zab_app_webitem")
        now_time = time.mktime(datetime.now().timetuple())

        dvalue = 0
        if re.search("h", end_time, flags=re.I):
            dvalue = int(end_time.split("h")[0])
        elif re.search("d", end_time, flags=re.I):
            dvalue = int(end_time.split("d")[0])*12
        else:
            dvalue = int(end_time.split("w")[0])*16

        time_till = now_time - 60 * 60 * int(dvalue)

        app_item_id = zab_web_itemids(app_name)

        res_hist_data = zab_web_item_data(item_name, app_item_id, now_time, time_till)

        return res_hist_data, 200, None