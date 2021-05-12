from sqlalchemy import Table, Column, Integer
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    strikes = Column(Integer, primary_key=True)
    points = Column(Integer, primary_key=True)

from bot import engine
Session = sessionmaker(bind=engine)
session = Session()
