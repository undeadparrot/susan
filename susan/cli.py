#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging

import click
from susan.config import bootstrap, get_config
from susan import api
from susan import db

import pyperclip

@click.group()
@click.option('--debug/--no-debug', default=True)
def cli(debug):
    config_path = os.path.join(
        click.get_app_dir('susan', 'config.ini', force_posix=True))
    bootstrap(filename=config_path)
    log_filename = get_config().get('logging', 'filename')
    logging.basicConfig(
        filename=log_filename, level=logging.DEBUG)
    if debug:
        logging.debug('Debug mode')


@cli.command()
def version():
    click.echo('Version: ')


@cli.command()
def cli_test():
    click.echo("test")


@cli.command()
@click.option("--topic", "-t", default=None, help="topic name")
def noted(topic):
    """Store a note (from editor) in a topic
    """
    if body:
        conn = db._ENGINE.connect()
        if not topic:
            topic = 'scratch'
        api.create_note(conn, body, topic=topic)
        conn.close()


@cli.command()
@click.option("--topic", "-t", default=None, help="topic name")
@click.option("--clipboard", "-p", is_flag=True, help="paste from clipboard")
@click.argument("body", required=False)
def note(body, topic, clipboard):
    """Store a note in a topic
    """
    conn = db._ENGINE.connect()
    if clipboard:
        body = pyperclip.paste()
    if not body:
        body = click.edit()
    if not body:
        return
    if not topic:
        topic = 'scratch'
    api.create_note(conn, body, topic=topic)
    conn.close()


@cli.command()
@click.option("--count", "-n", default=5, help="number of rows")
@click.option("--only-1", "-1", is_flag=True, help="only one row")
@click.option('--all-topics', is_flag=True)
@click.option("--clipboard", "-p", is_flag=True, help="copy to clipboard")
@click.argument("topic", required=False)
def head(count, only_1, topic, all_topics, clipboard):
    """Get the latest n notes in a topic
    """
    conn = db._ENGINE.connect()
    if not topic:
        topic = 'scratch'
    if all_topics:
        topic = None
    notes = api.list_notes(conn, limit=1 if only_1 else count, offset=0, topic=topic)
    conn.close()
    for note in notes:
        click.echo(note.body)
    if clipboard:
        pyperclip.copy("\n".join([_.body for _ in notes]))

