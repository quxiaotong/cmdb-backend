# -*- coding: utf-8 -*-

from cmdb.core.task.celery_base import celery
from flask import current_app as app

@celery.task()
def app_to_influx():
    from cmdb.core.task.ansible_handle_func import mem_top_10, cpu_top_10, system_cpu, system_mem
    result = mem_top_10()
    if result is True:
        print("mem_top_10 OK")
    result = cpu_top_10()
    if result is True:
        print("cpu_top_10 OK")
    result = system_cpu()
    if result is True:
        print("system_cpu OK")
    result = system_mem()
    if result is True:
        print("system_mem OK")
