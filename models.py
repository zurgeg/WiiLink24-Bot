from sqlalchemy import Table, Column, Integer, MetaData

meta = MetaData()

users = Table(
    Column('id', Integer, primary_key = True),
    Column('strikes', Integer),
    Column('points', Integer)
)

def init_db(engine):
    meta.create_all(engine)