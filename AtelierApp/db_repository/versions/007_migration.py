from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
events = Table('events', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64), nullable=False),
    Column('description', TEXT),
    Column('location', VARCHAR(length=256)),
    Column('date', DATE),
    Column('time', TIME),
    Column('places', INTEGER),
    Column('free', INTEGER),
    Column('active', BOOLEAN),
    Column('capacity', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].columns['free'].drop()
    pre_meta.tables['events'].columns['places'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['events'].columns['free'].create()
    pre_meta.tables['events'].columns['places'].create()
