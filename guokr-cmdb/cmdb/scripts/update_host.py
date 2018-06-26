# -*- coding: utf-8 -*-
import psycopg2
ansible_hosts = "/data/python/cmdb/ansible_ssh_hosts"
conn = psycopg2.connect(database="cmdb", user="postgres", password="cmdb", host="54.223.221.147", port="5432")
DBsession = conn.cursor()
DBsession.execute("select private_ip from ec2 where data_status is not FALSE")
res_ec2 = DBsession.fetchall()
conn.close()

def ansible_host_file():
    try:
        hostfile = open(ansible_hosts, 'w+', encoding='utf-8')
        for ec2 in res_ec2:
            hostfile.write(ec2[0]+"\n")
        hostfile.close()
    except Exception as e:
        print(e)
    else:
        print("ansible_hosts update successfully!")


