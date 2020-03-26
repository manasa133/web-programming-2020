from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.types import TIMESTAMP
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    name = Column(String(120), primary_key=True)
    passw = Column(String(50))
    time = Column(TIMESTAMP, nullable=False)

    def __init__(self, name, passw, time):
        self.name = name
        self.passw= passw
        self.time = time

    def __repr__(self):
        return '<User %r>' % (self.name)