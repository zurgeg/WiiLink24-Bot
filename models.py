from sqlalchemy import Table, Column, Integer, MetaData
from sqlalchemy.orm import sessionmaker
meta = MetaData()

users = Table(
    'users', meta,
    Column('id', Integer, primary_key = True),
    Column('strikes', Integer),
    Column('points', Integer)
)

def init_db(engine):
    meta.create_all(engine)
from bot import engine
Session = sessionmaker(bind=engine)
session = Session()
