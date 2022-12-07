from operator import index
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Username(Base):
    __tablename__ = 'student_name'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)