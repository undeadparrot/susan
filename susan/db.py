import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

_ENGINE = None

Base = declarative_base()
metadata = MetaData()

note_table = Table(
    "note",
    metadata,
    Column('note_id', Integer, primary_key=True),
    Column('topic', String),
    Column('body', String),
    Column('created', DateTime(timezone=True), server_default=func.now()), )


def bootstrap(get_config):
    connection_string = get_config().get('database', 'connection')
    logging.debug("Connection string: %s", connection_string)
    global _ENGINE
    _ENGINE = create_engine(connection_string)
    metadata.create_all(_ENGINE)
