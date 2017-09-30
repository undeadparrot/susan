#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from susan.config import bootstrap, get_config
from susan.db import note_table


def create_note(connection, body, topic):
    logging.debug("Creating note in :%s with body: %s", topic, body)
    connection.execute(note_table.insert(dict(body=body, topic=topic)))


def list_notes(connection, limit, offset, topic=None):
    logging.debug("List notes in :%s", topic)
    query = note_table.select().order_by(
        note_table.c.created.desc()).limit(limit).offset(offset)
    if topic:
        query = query.where(note_table.c.topic.ilike(topic))
    return connection.execute(query).fetchall()
