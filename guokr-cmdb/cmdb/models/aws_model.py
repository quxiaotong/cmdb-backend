# -*- coding: utf-8 -*-
from sqlalchemy.types import CHAR, Integer, String, Text, DateTime, Boolean, Enum
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import func, Table, UniqueConstraint
from cmdb.core.db import engine, Base, session, DBsession
from cmdb.v1.errors import abort

class Ec2(Base):
    __tablename__ = "ec2"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    instance_id = Column(String(64),
                         unique=True,
                         index=True,
                         nullable=False)
    private_ip = Column(String(64), nullable=True)
    public_ip = Column(String(64), nullable=True)
    run_state = Column(String(64), nullable=True)
    keyname = Column(String(64), nullable=True)
    name = Column(String(64), nullable=True)
    utilization = Column(String(64), nullable=True)
    data_status = Column(Boolean(), nullable=False,
                         index=True,default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    vpc_id = Column(Integer, ForeignKey("vpc.id"))
    instance_type = Column(String(64), ForeignKey("ec2type.type"))

    vpc = relationship("Vpc", backref="ec2")
    ec2_type = relationship("Ec2type", backref="ec2")


    def ec2_to_api(self, page_size, page_index):
        db_res_ec2 = DBsession.query(Ec2).filter(Ec2.data_status == True).order_by(Ec2.id).limit(page_size).offset((page_index-1)*page_size).all()
        for ec2_ins in db_res_ec2:
            cpu = ec2_ins.ec2_type.cpu
            memory = ec2_ins.ec2_type.memory
            ec2_ins.cpu_num = int(cpu)
            ec2_ins.memory_num = int(memory)
            ec2_ins.aws_create_time = ec2_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            ec2_ins.data_create_time = ec2_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            ec2_ins.data_update_time = ec2_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_ec2

    def detail_ec2(self, ip):
        ec2_ins = DBsession.query(Ec2).filter(Ec2.private_ip == ip).first()
        cpu = ec2_ins.ec2_type.cpu
        memory = ec2_ins.ec2_type.memory
        ec2_ins.cpu_num = int(cpu)
        ec2_ins.memory_num = int(memory)
        ec2_ins.aws_create_time = ec2_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
        ec2_ins.data_create_time = ec2_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
        ec2_ins.data_update_time = ec2_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return ec2_ins


class Vpc(Base):
    __tablename__ = "vpc"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    vpc_id = Column(String(64), unique=True,
                        index=True,
                    nullable=False)
    status = Column(String(64), nullable=False)
    cidrblock = Column(String(64), nullable=False)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    @property
    def vpc_to_api(self):
        db_res_vpc = DBsession.query(Vpc).filter(Vpc.data_status == True).order_by(Vpc.id).all()
        for vpc_ins in db_res_vpc:
            vpc_ins.data_create_time = vpc_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            vpc_ins.data_update_time = vpc_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_vpc

class Ec2type(Base):
    __tablename__ = "ec2type"
    type = Column(String(64), primary_key=True,
                  index=True, nullable=False)
    cpu = Column(Integer, nullable=False)
    memory = Column(Integer, nullable=False)


class Elasticache(Base):
    __tablename__ = "elasticache"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    cachecluster_id = Column(String(64), unique=True,
                             nullable=False, index=True)
    status = Column(String(64), nullable=False)
    engine = Column(String(64), nullable=False)
    data_status = Column(Boolean(), nullable=False,
                         index=True, default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    cachenode_type = Column(String(32), ForeignKey("ectype.type"))
    ec_type = relationship("Ectype", backref="elasticache")

    @property
    def ec_to_api(self):
        db_res_ec = DBsession.query(Elasticache).filter(Elasticache.data_status == True).order_by(Elasticache.id).all()
        for ec_ins in db_res_ec:
            memory = ec_ins.ec_type.memory
            ec_ins.memory_num = int(memory)
            ec_ins.aws_create_time = ec_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            ec_ins.data_create_time = ec_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            ec_ins.data_update_time = ec_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_ec


class Ectype(Base):
    __tablename__ = "ectype"
    type = Column(String(64), primary_key = True, index=True)
    memory = Column(Integer)

Ec2m2mElb = Table(
    'ec2m2melb',
    Base.metadata,
    Column("id",Integer, primary_key=True, index=True,autoincrement=True),
    Column("ec2_id", Integer, ForeignKey("ec2.id"), nullable=False,),
    Column("elb_id", Integer, ForeignKey("elb.id"), nullable=False,),
)

class Elb(Base):
    __tablename__ = "elb"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    loadbalancer_name = Column(String(64), unique=True, index=True)
    loadbalancer_port = Column(Integer)
    instance_port = Column(Integer)
    dns_name = Column(String(128),nullable=True,index=True,unique=True)
    data_status = Column(Boolean(), nullable=False,
                         index=True, default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    ec2 = relationship("Ec2",
                    secondary=Ec2m2mElb,
                    backref="elb")

    # vpc_id = Column(Integer, ForeignKey("vpc.id"))
    # vpc = relationship("Vpc", backref="elb")

    @property
    def elb_to_api(self):
        db_res_elb = DBsession.query(Elb).filter(Elb.data_status == True).order_by(Elb.id).all()
        for elb_ins in db_res_elb:
            elb_ins.aws_create_time = elb_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            elb_ins.data_create_time = elb_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            elb_ins.data_update_time = elb_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_elb


class Rds(Base):
    __tablename__ = "rds"
    id = Column(Integer, primary_key = True,
                autoincrement=True, nullable=True)
    db_identifier = Column(String(64), nullable=False, index=True,unique=True)
    status = Column(String(64), nullable=False)
    engine = Column(String(64), nullable=False)
    resource_id = Column(String(64), unique = True, nullable=False)
    storage_type = Column(String(64), nullable=False)
    data_status = Column(Boolean(64), nullable=False,
                         index=True, default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    instance_type = Column(String(64), ForeignKey("rdstype.type"))
    vpc_id = Column(Integer, ForeignKey("vpc.id"))

    rds_type = relationship("Rdstype", backref="rds")
    vpc = relationship("Vpc", backref="rds")

    @property
    def rds_to_api(self):
        db_res_rds = DBsession.query(Rds).filter(Rds.data_status == True).order_by(Rds.id).all()
        for rds_ins in db_res_rds:
            cpu = rds_ins.rds_type.cpu
            memory = rds_ins.rds_type.memory
            rds_ins.cpu = int(cpu)
            rds_ins.memory = int(memory)
            rds_ins.aws_create_time = rds_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            rds_ins.data_create_time = rds_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            rds_ins.data_update_time = rds_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_rds


class Rdstype(Base):
    __tablename__ = "rdstype"
    type = Column(String(64), primary_key = True, index=True)
    cpu = Column(Integer, nullable=False)
    memory = Column(Integer, nullable=False)


class Volume(Base):
    __tablename__ = "volume"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    volume_id = Column(String(64),unique=True,
                       index=True, nullable=False)
    size = Column(Integer(), nullable=False)
    state = Column(String(64), nullable=False)
    iops = Column(String(64), nullable=True)
    volume_type = Column(String(64), nullable=False)
    device = Column(String(64), nullable=False)
    ec2_instance_id = Column(String(64), nullable=False)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    ec2_instance_name = Column(String(64), index=True, nullable=True)

    @property
    def vol_to_api(self):
        db_res_vol = DBsession.query(Volume).filter(Volume.data_status == True).order_by(Volume.id).all()
        for vol_ins in db_res_vol:
            vol_ins.aws_create_time = vol_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            vol_ins.data_create_time = vol_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            vol_ins.data_update_time = vol_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_vol

class S3(Base):
    __tablename__ = "s3"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique = True, nullable=False)
    size = Column(String(64), nullable=False)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    @property
    def s3_to_api(self):
        db_res_s3 = DBsession.query(S3).filter(S3.data_status == True).order_by(S3.id).all()
        for s3_ins in db_res_s3:
            s3_ins.aws_create_time = s3_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            s3_ins.data_create_time = s3_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            s3_ins.data_update_time = s3_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_s3

class Iam(Base):
    __tablename__ = "iam"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(64), nullable=False, unique=True)
    user_name = Column(String(64), nullable=False, unique=True)
    password_lastused = Column(String(64),nullable=True)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    aws_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    @property
    def iam_to_api(self):
        db_res_iam = DBsession.query(Iam).filter(Iam.data_status == True).order_by(Iam.id).all()
        for iam_ins in db_res_iam:
            iam_ins.aws_create_time = iam_ins.aws_create_time.strftime("%Y-%m-%d %H:%M:%S")
            iam_ins.data_create_time = iam_ins.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            iam_ins.data_update_time = iam_ins.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return db_res_iam


class App(Base):
    __tablename__ = 'app'
    id = Column(Integer(), nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False, unique=True)
    desc = Column(Text(), nullable=True, index=False)
    project = Column(String(64), nullable=True, unique=False)

    def get_sysconfig(self, app_name):
        try:
            res_app = DBsession.query(App).filter(App.name == app_name).first()
            res_sysconfig = res_app.sysconfig
            for res in res_sysconfig:
                res.data_update_time = res.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
            return res_sysconfig
        except Exception as e:
            abort("app_name not find")


class App2Aws(Base):
    __tablename__ = 'app_to_resource'
    id = Column(Integer(), nullable=False,
                primary_key=True,autoincrement=True)
    app_id = Column(Integer, ForeignKey('app.id'), nullable=True, index=True)
    resource_id = Column(Integer, nullable=True, index=True)
    resource_type = Column(Enum("elb", "ec2", "redis", "rds", "s3", name="resource_type"), nullable=False)
    listen_port = Column(String(64),nullable=True,unique=False)
    project = Column(String(64),nullable=True,unique=False)
    host_ip = Column(String(64),nullable=True,unique=False)
    __table_args__ = (UniqueConstraint('app_id', 'resource_type', 'resource_id','listen_port', name='app_resource'),)



class OpsAccountManage(Base):
    __tablename__ = 'ops_account_manage'
    id = Column(Integer(), nullable=False,
                primary_key=True,autoincrement=True)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    platform = Column(Text(), nullable=False,)
    account = Column(String(64), nullable=False,)
    secret = Column(String(64), nullable=False,)
    mark = Column(Text(), nullable=True,)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    @property
    def get_accunt(self):
        res_acc = DBsession.query(OpsAccountManage).filter(OpsAccountManage.data_status == True).order_by(OpsAccountManage.id).all()
        for res in res_acc:
            res.platform = str(res.platform)
            res.mark = str(res.mark)
            res.data_create_time = res.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            res.data_update_time = res.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return res_acc


class WinXinAcount(Base):
    __tablename__ = 'wx_account_manage'
    id = Column(Integer(), nullable=False,
                primary_key=True,autoincrement=True)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)

    use_type = Column(Text(), nullable=False,)
    name = Column(Text(), nullable=False,)
    type = Column(Text(), nullable=False,)
    mail = Column(String(64), nullable=False,)
    secret = Column(String(64), nullable=False,)
    use_name = Column(String(64), nullable=False,)
    phone = Column(String(64), nullable=False,)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    @property
    def get_accunt(self):
        res_acc = DBsession.query(WinXinAcount).filter(WinXinAcount.data_status == True).order_by(WinXinAcount.id).all()
        for res in res_acc:
            res.data_create_time = res.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
            res.data_update_time = res.data_update_time.strftime("%Y-%m-%d %H:%M:%S")
        return res_acc

class CmdbUser(Base):
    __tablename__ = "cmdb_user"
    id = Column(Integer(), nullable=False,
                primary_key=True, autoincrement=True)
    data_status = Column(Boolean(), index=True,
                         nullable=False, default=True)
    account = Column(String(64), unique=True,
                       index=True, nullable=False)
    secret = Column(String(64), index=True, nullable=False)
    authority = Column(String(64), index=True, nullable=False)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())
    @property
    def get_accunt(self):
        res_acc = DBsession.query(CmdbUser).filter(CmdbUser.data_status == True).order_by(CmdbUser.id).all()
        for res in res_acc:
            res.data_create_time = res.data_create_time.strftime("%Y-%m-%d %H:%M:%S")
        return res_acc


class sysconfig(Base):
    __tablename__ = 'sysconfig_manage'
    id = Column(Integer(), nullable=False,
                primary_key=True,autoincrement=True)
    key = Column(Text(), nullable=False, unique=True, index=True)
    value = Column(Text(), nullable=False,)
    user_name = Column(String(64), nullable=False,)
    data_update_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())

    app_id = Column(Integer, ForeignKey("app.id"))
    app = relationship("App", backref="sysconfig")



class LogCrontab(Base):
    __tablename__ = 'log'
    id = Column(Integer(), nullable=False,
                primary_key=True,autoincrement=True)
    content = Column(Text(), nullable=True, index=False)
    data_create_time = Column(DateTime(timezone=True),
                           nullable=False, index=True,
                           server_default=func.current_timestamp())


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

#init_db()