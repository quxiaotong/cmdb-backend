# -*- coding: utf-8 -*-
from cmdb.core.ansible_base import AnsibleTask

from cmdb.core.task.ansible_tasks_to_db import app
from cmdb.core.db import influxdb_client


json_body = [
        {
            "measurement": "",
            "tags": {
                "": ""
            },
            "fields": {
            },
        }
    ]

def app_mem_top(host, result):
    final_result = {host:[]}
    for item in result[host]:
        process_data = {}
        item = item.split()
        process_data["pid"] = item[0]
        process_data["mem_percent"] = item[1]
        process_data["name"] = str(item[2]).split('/')[-1]
        final_result[host].append(process_data)
    try:
        for data in final_result[host]:
            json_body[0]["measurement"] = "app_mem_top"
            json_body[0]["tags"]["pid"] = data["pid"]
            json_body[0]["tags"]["process_name"] = data["name"]
            json_body[0]["tags"]["host"] = host
            json_body[0]["fields"]["mem_percent"] = data["mem_percent"]
            influxdb_client.write_points(json_body)
    except Exception as e:
        print(e)
    else:
        print("app_mem_top'data handle OK")


def app_cpu_top(host, result):
    final_result = {host:[]}
    for item in result[host]:
        process_data = {}
        item = item.split()
        process_data["pid"] = item[0]
        process_data["cpu_percent"] = item[1]
        process_data["name"] = str(item[2]).split('/')[-1]
        final_result[host].append(process_data)
    try:
        for data in final_result[host]:
            json_body[0]["measurement"] = "app_cpu_top"
            json_body[0]["tags"]["pid"] = data["pid"]
            json_body[0]["tags"]["process_name"] = data["name"]
            json_body[0]["tags"]["host"] = host
            json_body[0]["fields"]["cpu_percent"] = data["cpu_percent"]
            influxdb_client.write_points(json_body)
    except Exception as e:
        print(e)
    else:
        print("app_mem_top'data handle OK")

def system_cpu_data_handle(host, result):
    final_result = {host:[]}
    for item in result[host]:
        process_data = {}
        item = item.split()
        process_data["user_cpu"] = item[0]
        process_data["sys_cpu"] = item[1]
        process_data["idle_cpu"] = item[2]
        final_result[host].append(process_data)
    try:
        for data in final_result[host]:
            json_body[0]["measurement"] = "system_ec2_cpu"
            json_body[0]["fields"]["user_cpu"] = float(data["user_cpu"])
            json_body[0]["fields"]["sys_cpu"] = float(data["sys_cpu"])
            json_body[0]["fields"]["idle_cpu"] = float(data["idle_cpu"])
            json_body[0]["tags"]["host"] = host
            influxdb_client.write_points(json_body)
    except Exception as e:
        print(e)
    else:
        print("system_cpu'data handle OK")

def system_memery_data_handle(host, result):
    final_result = {host:[]}
    for item in result[host]:
        process_data = {}
        item = item.split()
        process_data["total"] = item[0]
        process_data["used"] = item[1]
        process_data["free"] = item[2]
        process_data["shared"] = item[3]
        final_result[host].append(process_data)

    try:
        for data in final_result[host]:
            json_body[0]["measurement"] = "system_ec2_memery"
            json_body[0]["fields"]["used"] = float("%.3f" % (int(data["used"])/int(data["total"])))
            json_body[0]["fields"]["free"] = float("%.3f" % (int(data["free"])/int(data["total"])))
            json_body[0]["fields"]["shared"] = float("%.3f" % (int(data["shared"])/int(data["total"])))
            json_body[0]["tags"]["host"] = host
            influxdb_client.write_points(json_body)
    except Exception as e:
        print(e)
    else:
        print("system_memery'data handle OK")

def mem_top_10():
    memery_top_10 = AnsibleTask()
    try:
        memery_top_10.play_task("raw", "ps aux|grep -v PID| awk '{print $2,$4,$11}' | sort -rn -k +2|head -10", "mem_top_10", app_mem_top)
    except Exception as e:
        print(e)
    else:
        return True

def cpu_top_10():
    cpu_top_10 = AnsibleTask()
    try:
        cpu_top_10.play_task("raw", "ps aux|grep -v PID| awk '{print $2,$3,$11}' | sort -rn -k +2|head -10", "cpu_top_10", app_cpu_top)
    except Exception as e:
        print(e)
    else:
        return True

def system_cpu():
    system_cpu_task = AnsibleTask()
    try:
        system_cpu_task.play_task("raw", "vmstat  | grep -v 'io'| grep -v 'us' | awk  '{print $13,$14,$15}'", "system_cpu", system_cpu_data_handle)
    except Exception as e:
        print(e)
    else:
        return True

def system_mem():
    system_mem_task = AnsibleTask()
    try:
        system_mem_task.play_task("raw", "free | grep -i mem | awk '{print $2,$3,$4,$5}'", "system_mem", system_memery_data_handle)
    except Exception as e:
        print(e)
    else:
        return True