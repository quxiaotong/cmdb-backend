from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.types import CHAR,Integer,String,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import func
import psycopg2
engine = create_engine('postgresql://zaihang:zzzz@10.0.80.13:5432/cmdb',echo=True)
Base = declarative_base()

class Ec2(Base):
    __tablename__="ec2"
    instance_id=Column(String(64),primary_key=True)
    private_ip=Column(String(64))
    public_ip=Column(String(64))
    run_state=Column(String(64))
    keyname=Column(String(64))
    create_time=Column(String(64))

    vpc_id=Column(String(64),ForeignKey("vpc.vpc_id"))
    instance_type=Column(String(64),ForeignKey("ec2type.type"))

    vpc=relationship("Vpc",backref="ec2")
    ec2_type=relationship("Ec2type",backref="ec2")



class Vpc(Base):
    __tablename__="vpc"
    vpc_id=Column(String(64),primary_key=True)
    status=Column(String(64))
    cidrblock=Column(String(64))


class Ec2type(Base):
    __tablename__="ec2type"
    type=Column(String(64),primary_key=True)
    cpu=Column(Integer)
    memory=Column(Integer)


class Elasticache(Base):
    __tablename__="elasticache"
    id=Column(Integer,primary_key=True)
    cachecluster_id=Column(String(64),unique=True,nullable=False)
    create_time=Column(String(64))
    status=Column(String(64))
    engine=Column(String(64))

    cachenode_type=Column(String(32),ForeignKey("ectype.type"))
    ec_type=relationship("Ectype",backref="elasticache")

class Ectype(Base):
    __tablename__="ectype"
    type=Column(String(64),primary_key=True)
    memory=Column(Integer)



class Elb(Base):
    __tablename__="elb"
    id=Column(Integer,primary_key=True)
    loadbalancer_name=Column(String(64))
    loadbalancer_port=Column(Integer)
    instance_port=Column(Integer)
    created_time=Column(String(64))
    dns_name=Column(String(128),unique=True,nullable=False)

    vpc_id=Column(String(64),ForeignKey("vpc.vpc_id"))
    vpc=relationship("Vpc",backref="elb")

class Rds(Base):
    __tablename__="rds"
    id=Column(Integer,primary_key=True)
    db_identifier=Column(String(64))
    status=Column(String(64))
    engine=Column(String(64))
    resource_id=Column(String(64),unique=True,nullable=False)
    create_time=Column(String(64))
    storage_type=Column(String(64))

    instance_type=Column(String(64),ForeignKey("rdstype.type"))
    vpc_id=Column(String(64),ForeignKey("vpc.vpc_id"))

    rds_type=relationship("Rdstype",backref="rds")
    vpc=relationship("Vpc",backref="rds")

class Rdstype(Base):
    __tablename__="rdstype"
    type=Column(String(64),primary_key=True)
    cpu=Column(Integer)
    memory=Column(Integer)

class Volume(Base):
    __tablename__="volume"
    volume_id=Column(String(64),primary_key=True)
    size=Column(String(64))
    state=Column(String(64))
    create_time=Column(String(64))
    iops=Column(String(64))
    volume_type=Column(String(64))

    ec2_instance_id=Column(String(64),ForeignKey("ec2.instance_id"))

    ec2=relationship("Ec2",backref="volume")



class S3(Base):
    __tablename__="s3"
    id=Column(Integer,primary_key=True)
    creation_date=Column(String(64))
    name=Column(String(64),unique=True,nullable=False)
    size=Column(String(64))

class Iam(Base):
    __tablename__="iam"
    id=Column(Integer,primary_key=True)
    user_id=Column(String(64))
    user_name=Column(String(64))
    password_lastused=Column(String(64))
    create_date=Column(String(64))


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

session = sessionmaker(bind=engine)
DBsession=session()

#init_db()





