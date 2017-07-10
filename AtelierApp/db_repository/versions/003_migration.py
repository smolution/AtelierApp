from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
categories = Table('categories', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64), nullable=False),
)

collections = Table('collections', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64), nullable=False),
)

photos = Table('photos', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('filename', String(length=64), nullable=False),
    Column('filepath', String(length=256)),
    Column('slideshow', Boolean, default=ColumnDefault(False)),
    Column('active', Boolean, default=ColumnDefault(True)),
    Column('featured', Boolean, default=ColumnDefault(False)),
    Column('collection_id', Integer),
    Column('category_id', Integer),
    Column('subcategory_id', Integer),
)

subcategories = Table('subcategories', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64), nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['categories'].create()
    post_meta.tables['collections'].create()
    post_meta.tables['photos'].create()
    post_meta.tables['subcategories'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['categories'].drop()
    post_meta.tables['collections'].drop()
    post_meta.tables['photos'].drop()
    post_meta.tables['subcategories'].drop()
