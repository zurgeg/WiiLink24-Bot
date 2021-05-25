from sqlalchemy import Table, Column, Integer, create_engine, Boolean
from sqlalchemy.orm import sessionmaker
import config
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    strikes = Column(Integer)
    points = Column(Integer)
    muted = Column(Boolean, default=False)


engine = create_engine(config.db_url)
Session = sessionmaker(bind=engine)
session = Session()
