from cmdb.core.task.celery_base import celery

@celery.task()
def etcdtodb():
    import etcd
    from cmdb.models import aws_model
    etcd_client = etcd.Client(host="54.223.98.251",port=2379)

    def etcd_services():
        services_names = []
        services_addrs = {}
        services_kv = {}
        services = etcd_client.read("/services")._children
        for service in services:
            service_name = service["key"].split("/")[-1]
            services_names.append(service_name)
            service_addrs = etcd_client.read("/services/" + service_name + "/address")._children
            services_addrs[service_name] = []
            services_kv[service_name] = []
            for service_addr in service_addrs:
                service_addr = service_addr["key"].split("/")[-1]
                services_addrs[service_name].append(service_addr)
                services_kv[service_name].append({service_addr:etcd_client.read("/services/" + service_name + "/address/"+service_addr).value})
        return services_names, services_addrs, services_kv

    existappnames = []
    existapps = aws_model.DBsession.query(aws_model.App).all()
    for app in existapps:
        existappnames.append(app.name)
    services_names, services_addrs, services_kv= etcd_services()
    for service_name in services_names:
        if service_name not in existappnames:
            appinst = aws_model.App(name=service_name)
            aws_model.DBsession.add(appinst)
            try:
                aws_model.DBsession.commit()
            except Exception as e:
                print(e)
                aws_model.DBsession.rollback()
            for service_addr in services_addrs[service_name]:
                serid = aws_model.DBsession.query(aws_model.App.id).filter(aws_model.App.name == service_name).first()[0]
                # for values in services_kv[service_name]:
                #     for item in values:
                #         if item == service_addr:
                #             value = values[service_addr].split(":")
                app2aws_inst = aws_model.App2Aws(app_id=serid, resource_id=service_addr, resource_type="ec2", project=service_addr[2], listen_port=service_addr[1], host_ip=service_addr[0])
                aws_model.DBsession.add(app2aws_inst)
                try:
                    aws_model.DBsession.commit()
                except Exception as e:
                    print(e)
                    aws_model.DBsession.rollback()

        else:
            ser_id = aws_model.DBsession.query(aws_model.App.id).filter(aws_model.App.name == service_name).first()[0]
            service_db_ips_set = set()
            service_db_ips = aws_model.DBsession.query(aws_model.App2Aws.resource_id).join(aws_model.App, aws_model.App.id == aws_model.App2Aws.app_id).\
                        filter(aws_model.App.name == service_name, aws_model.App2Aws.resource_type=="ec2").all()
            service_now_ips_set = set(services_addrs[service_name])
            for service_db_ip in service_db_ips:
                service_db_ips_set.add(service_db_ip[0])
            add_ips = service_now_ips_set - service_db_ips_set
            del_ips = service_db_ips_set - service_now_ips_set
            for add_ip in add_ips:
                try:
                    project_name = aws_model.DBsession.query(aws_model.App2Aws.project).filter(aws_model.App2Aws.app_id == ser_id).first()[0]
                except Exception:
                    for item in services_kv[service_name]:
                        for ip in item:
                            if add_ip == ip:
                                project_name = ip.split(":")[2]
                app2aws_inst = aws_model.App2Aws(app_id=ser_id, resource_id=add_ip, resource_type="ec2", listen_port=add_ip.split(":")[1], project=project_name, host_ip=add_ip.split(":")[0])
                aws_model.DBsession.add(app2aws_inst)
                try:
                    aws_model.DBsession.commit()
                except Exception:
                    aws_model.DBsession.rollback()
            for del_ip in del_ips:
                aws_model.DBsession.query(aws_model.App2Aws).filter(aws_model.App2Aws.resource_id == del_ip, aws_model.App2Aws.app_id==ser_id,aws_model.App2Aws.resource_type == "ec2").delete()
                try:
                    aws_model.DBsession.commit()
                except Exception:
                    aws_model.DBsession.rollback()
