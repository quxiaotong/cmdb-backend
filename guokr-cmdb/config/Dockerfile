FROM 180.76.244.5/quxiaotong/cmdb:base_pip_ok
ADD guokr-cmdb.tar.gz /data/python/cmdb
WORKDIR /data/python/cmdb/guokr-cmdb
RUN pip3 install -r requirements.txt
WORKDIR /data/python/cmdb/guokr-cmdb
CMD ["python3.5","manage.py","server"]
