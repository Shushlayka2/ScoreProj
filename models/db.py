# coding: utf-8
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime 

engine = create_engine('postgresql://postgres:asehan57@localhost:5432/postgres', echo = True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
metadata = Base.metadata


class Institute(Base):
    __tablename__ = 'institute'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('institute_id_seq'::regclass)"))
    name = Column(String(40))


class Scope(Base):
    __tablename__ = 'scope'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('scope_id_seq'::regclass)"))
    name = Column(String(30), nullable=False)


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('department_id_seq'::regclass)"))
    name = Column(String(40))
    institute_id = Column(ForeignKey('institute.id'), nullable=False)

    institute = relationship('Institute')


class Professor(Base):
    __tablename__ = 'professor'

    full_name = Column(String(60), nullable=False)
    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('professor_id_seq'::regclass)"))
    is_expert = Column(Boolean, nullable=False, server_default=text("false"))
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    department_id = Column(ForeignKey('department.id'), nullable=False)

    department = relationship('Department')


class Diploma(Base):
    __tablename__ = 'diploma'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('diploma_id_seq'::regclass)"))
    thesis = Column(String(90), nullable=False)
    description = Column(Text, nullable=False)
    deadline = Column(Date, nullable=False)
    team_work = Column(Boolean, nullable=False, server_default=text("false"))
    evaluation = Column(Integer)
    publish_time = Column(Date, nullable=False)
    professor_id = Column(ForeignKey('professor.id'), nullable=False)
    scope_id = Column(ForeignKey('scope.id'))

    professor = relationship('Professor')
    scope = relationship('Scope')

class Criterion(Base):
    __tablename__ = 'criteria'

    id = Column(Integer, primary_key=True, unique=True, server_default=text("nextval('criteria_id_seq'::regclass)"))
    thesis_ev = Column(Integer, nullable=False)
    relevance_ev = Column(Integer, nullable=False)
    interest_ev = Column(Integer, nullable=False)
    feasibility_ev = Column(Integer, nullable=False)
    expert_id = Column(ForeignKey('professor.id'), nullable=False)
    diploma_id = Column(ForeignKey('diploma.id'), nullable=False)

    diploma = relationship('Diploma')
    expert = relationship('Professor')