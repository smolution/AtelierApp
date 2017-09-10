from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
events = Table('events', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64), nullable=False),
    Column('description', Text),
    Column('location', String(length=256)),
    Column('date', Date),
    Column('time', Time),
    Column('places', Integer),
    Column('free', Integer),
    Column('active', Boolean, default=ColumnDefault(True)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['events'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['events'].drop()
