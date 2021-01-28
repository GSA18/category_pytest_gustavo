from sqlalchemy import Column, Integer
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id_ = Column('id', Integer, primary_key=True)
