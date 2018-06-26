# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C
import sys
import datetime
import psycopg2
from influxdb import InfluxDBClient
import json

import os
import psutil
import datetime
import json
def app_cpu_top():
    now_time = datetime.datetime.now()
    now = datetime.datetime.strftime(now_time,"%Y.%m.%d %H:%M:%S")
    res = os.popen("ps aux|grep -v PID| awk '{print $2,$3}' | sort -rn -k +2|head -10").read().split("\n")
    res_cpu = [item.split(" ") for item in res[:-1]]
    res_data = []
    for item in res_cpu:
        process_data = {}
        process_data["pid"] = item[0]
        process_data["cpu_percent"] = item[1]
        try:
            item.append(psutil.Process(int(item[0])).name())
        except Exception:
            process_data["name"] = "None"
        else:
            process_data["name"] = item[2]
        res_data.append(process_data)
    res_data.append({"now_time":now})
    res = json.dumps(res_data)
    print(res)

def app_memery_top():
    now_time = datetime.datetime.now()
    now = datetime.datetime.strftime(now_time,"%Y.%m.%d %H:%M:%S")
    res = os.popen("ps aux|grep -v PID| awk '{print $2,$4}' | sort -rn -k +2|head -10").read().split("\n")
    res_cpu = [item.split(" ") for item in res[:-1]]
    res_data = []
    for item in res_cpu:
        process_data = {}
        process_data["pid"] = item[0]
        process_data["memery_percent"] = item[1]
        try:
            item.append(psutil.Process(int(item[0])).name())
        except Exception:
            process_data["name"] = "None"
        else:
            process_data["name"] = item[2]
        res_data.append(process_data)
    res_data.append({"now_time":now})
    res = json.dumps(res_data)
    print(res)


def system_cpu():
    res_data = []
    now_time = datetime.datetime.now()
    now = datetime.datetime.strftime(now_time,"%Y.%m.%d %H:%M:%S")
    res = os.popen("vmstat  | grep -v 'io'| grep -v 'us' | awk  '{print $13,$14,$15}'").read().split("\n")
    res_cpu = [item.split(" ") for item in res[:-1]]
    res_data.append({"user_cpu":res_cpu[0][0]})
    res_data.append({"sys_cpu":res_cpu[0][1]})
    res_data.append({"idle_cpu":res_cpu[0][2]})
    res_data.append({"now_time":now})
    res = json.dumps(res_data)
    print(res)

def system_memery():
    res_data = []
    now_time = datetime.datetime.now()
    now = datetime.datetime.strftime(now_time,"%Y.%m.%d %H:%M:%S")
    res = os.popen("free | grep -i mem | awk '{print $2,$4}'").read().split("\n")
    res_cpu = [item.split(" ") for item in res[:-1]]
    free_memery = int(int(res_cpu[0][1])/1024)
    free_memery_retio = float("%.3f" % (int(res_cpu[0][1])/int(res_cpu[0][0])))
    res_data.append({"free_memery":free_memery})
    res_data.append({"free_memery_retio":free_memery_retio})
    res_data.append({"now_time":now})
    res = json.dumps(res_data)
    print(res)

def collect():
    try:
        system_cpu()
        app_cpu_top()

        system_memery()
        app_memery_top()
    except Exception as e:
        print(e)


influxdb_client = InfluxDBClient('127.0.0.1',8086 ,'cmdb','cmdb','cmdb')
ansible_hosts = "/data/python/cmdb/test"
#conn = psycopg2.connect(database="cmdb", user="postgres", password="cmdb", host="54.223.221.147", port="5432")
#DBsession = conn.cursor()
#DBsession.execute("select private_ip from ec2 where data_status is not FALSE")
#res_ec2 = DBsession.fetchall()
#conn.close()


#def ansible_host_file():
#    try:
#        hostfile = open(ansible_hosts, 'w+', encoding='utf-8')
#        for ec2 in res_ec2:
#            hostfile.write(ec2[0]+"\n")
#        hostfile.close()
#    except Exception as e:
#        print(e)
#    else:
#        return True

class ResultCallback(CallbackBase):

    def __init__(self, display, options, result_function, task_name):
        super(ResultCallback,self).__init__(display, options)
        self.result_function = result_function
        self.task_name = task_name

    def v2_runner_on_unreachable(self, result):
        host = result._host.get_name()
        self.runner_on_unreachable(host, result._result)
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + "this host " + host + " is not unreachable")

    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" +  json.dumps({host.name: result._result, "error": ignore_errors}))

    def v2_runner_on_ok(self, result, **kwargs):
        try:
            handle_result = {}
            host = result._host
            res_task = {host.name:result._result}
            handle_result[host.name] = res_task[host.name]["stdout_lines"]
            self.result_function(host.name, handle_result)
        except Exception as e:
            now = datetime.datetime.now()
            print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + e)


class AnsibleTask(object):
    def __init__(self,ansible_host):
        self.ansible_host = ansible_host
        res = True
        if res is True:
            Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become',
                                             'become_method', 'become_user', 'check', 'diff'])
            self.options = Options(connection='ssh', module_path=sys.path, forks=100, become=None,
                                   become_method=None, become_user=None, check=False,diff=False)
            self.passwords = dict(vault_pass='secret')
            self.loader = DataLoader()
            self.inventory = InventoryManager(loader=self.loader, sources=self.ansible_host)
            self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)


    def play_task(self, module, args, task_name, function):
        results_callback = ResultCallback(display=None, options=None, task_name=task_name, result_function=function)

        play_source = dict(
                name=task_name,
                hosts='all',
                gather_facts='no',
                tasks=[
                    dict(action=dict(module=module, args=args), register='shell_out'),
                    #dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
                 ]
            )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)
        tqm = None
        try:
            tqm = TaskQueueManager(
                      inventory=self.inventory,
                      variable_manager=self.variable_manager,
                      loader=self.loader,
                      options=self.options,
                      passwords=self.passwords,
                      stdout_callback=results_callback,
                  )
            result = tqm.run(play)
        except Exception as e:
            now = datetime.datetime.now()
            print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + e)
        # else:
        #     return True
        finally:
            if tqm is not None:
                tqm.cleanup()
            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

json_body = [
        {
            "measurement": "",
            "tags": {
            },
            "time":"",
            "fields": {
            },
        }
    ]

def data_to_influxdb(host, result):
    try:
        system_cpu = json.loads(result[host][0])
        app_cpu = json.loads(result[host][1])
        system_memery = json.loads(result[host][2])
        app_memery = json.loads(result[host][3])
        try:
            json_body[0]["measurement"] = "system_cpu"
            json_body[0]["fields"]["user_cpu"] = system_cpu[0]["user_cpu"]
            json_body[0]["fields"]["sys_cpu"] = system_cpu[1]["sys_cpu"]
            json_body[0]["fields"]["idle_cpu"] = system_cpu[2]["idle_cpu"]
            json_body[0]["tags"]["host"] = host
            json_body[0]["time"] = system_cpu[3]["now_time"]
            influxdb_client.write_points(json_body)
        except Exception as e:
            print(e)

        for data in app_cpu[:-1]:
            json_body[0]["measurement"] = "app_cpu_top"
            json_body[0]["tags"]["pid"] = data["pid"]
            json_body[0]["tags"]["process_name"] = data["name"]
            json_body[0]["tags"]["host"] = host
            json_body[0]["fields"]["cpu_percent"] = data["cpu_percent"]
            json_body[0]["time"] = app_cpu[-1]["now_time"]
            influxdb_client.write_points(json_body)

        try:
            json_body[0]["measurement"] = "system_memery"
            json_body[0]["tags"]["host"] = host
            json_body[0]["fields"]["free_memery"] = system_memery[0]["free_memery"]
            json_body[0]["fields"]["free_memery_retio"] = system_memery[1]["free_memery_retio"]
            json_body[0]["time"] = system_memery[2]["now_time"]
            influxdb_client.write_points(json_body)
        except Exception as e:
            print(e)

        for data in app_memery[:-1]:
            json_body[0]["measurement"] = "app_memery_top"
            json_body[0]["tags"]["pid"] = data["pid"]
            json_body[0]["tags"]["process_name"] = data["name"]
            json_body[0]["tags"]["host"] = host
            json_body[0]["fields"]["memery_percent"] = data["memery_percent"]
            json_body[0]["time"] = app_memery[-1]["now_time"]
            influxdb_client.write_points(json_body)

    except Exception as e:
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + e)
    else:
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + " app_cpu_top'data handle OK")

def cpu_top_10():
    cpu_top_10 = AnsibleTask(ansible_hosts)
    try:
        cpu_top_10.play_task("shell", "python /root/ansible_task.py", "ansible_task", data_to_influxdb)
    except Exception as e:
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + e)
    else:
        return True

def app_to_influx():
    result = cpu_top_10()
    if result is True:
        now = datetime.datetime.now()
        print(datetime.datetime.strftime(now,"%Y.%m.%d %H:%M:%S") + ":" + " cpu_top_10 OK")
# if __name__ == '__main__':
#     app_to_influx()