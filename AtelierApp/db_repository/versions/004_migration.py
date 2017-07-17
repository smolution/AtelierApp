from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
subcategories = Table('subcategories', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('fullname', String(length=64)),
)

collections = Table('collections', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('fullname', String(length=64)),
)

categories = Table('categories', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('fullname', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subcategories'].columns['fullname'].create()
    post_meta.tables['collections'].columns['fullname'].create()
    post_meta.tables['categories'].columns['fullname'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['subcategories'].columns['fullname'].drop()
    post_meta.tables['collections'].columns['fullname'].drop()
    post_meta.tables['categories'].columns['fullname'].drop()
