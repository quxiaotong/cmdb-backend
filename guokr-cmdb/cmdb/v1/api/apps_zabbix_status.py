# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import time
from datetime import datetime
from cmdb.core.zabbix_web import zab_web_itemids, zab_web_item_data, zab_web_apps_name, zab_web_item_trend


class AppsZabbixStatus(Resource):

    def get(self):
        now_time = time.mktime(datetime.now().timetuple())
        time_till = now_time - 60 * 60 * 2
        code_time_till = now_time - 60 * 60 * 1

        res_data = [{}]
        for app_name in zab_web_apps_name:

            app_web_item_id = zab_web_itemids(app_name)
            response_code = zab_web_item_data("response_code", app_web_item_id, now_time, code_time_till)
            code_all = response_code[0]["data"]
            code_per = int((code_all.count("200")/len(code_all))*100//1)

            app_item_trend_data = {}
            for item in app_web_item_id:
                trend_data = zab_web_item_trend(item, app_web_item_id, now_time, time_till)
                app_item_trend_data[item] = trend_data
            app_item_trend_data["response_code"] = {"200": code_per, "other": (100 - code_per)}
            res_data[0][app_name] = app_item_trend_data

        return res_data, 200, None