from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (CheckConstraint, UniqueConstraint,
                        Column, DateTime, Integer, String)
from sqlalchemy import create_engine, desc
from datetime import datetime
import os
import sys

sys.path.append(os.getcwd())


engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()


class Student(Base):
    __tablename__ = 'scholars'

    id = Column(Integer(), primary_key=True)
    full_name = Column(String(), index=True)
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"
