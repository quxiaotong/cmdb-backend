FROM 180.76.244.5/quxiaotong/cmdb:base_pip_ok
ADD guokr-cmdb.tar.gz /data/python/cmdb
WORKDIR /data/python/cmdb/guokr-cmdb
RUN pip3 install -r requirements.txt
RUN pip3 install elastic-apm[flask]
RUN pip3 install supervisor
WORKDIR /data/python/cmdb/guokr-cmdb
