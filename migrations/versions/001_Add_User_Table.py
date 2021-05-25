from sqlalchemy import *
from migrate import *
meta = MetaData()

users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column("strikes", Integer),
    Column("points", Integer),
    Column("muted", Boolean)
)
def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pass
