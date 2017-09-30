import logging
import configparser

import susan.db
_CONFIG = None


def bootstrap(filename):
    """Reads config and prepares db pool"""
    logging.debug("Bootstrap from %s", filename)
    global _CONFIG
    _CONFIG = configparser.ConfigParser()
    _CONFIG.read(filename)
    susan.db.bootstrap(get_config)


def get_config():
    return _CONFIG
