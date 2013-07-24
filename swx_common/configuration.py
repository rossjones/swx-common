import os
import ConfigParser

CONFIG_ENV = 'SWX_CONFIG'

if not CONFIG_ENV in os.environ:
    raise ImportError('Unable to load config, SWX_CONFIG is not set')

if not os.path.exists(os.environ[CONFIG_ENV]):
    raise ImportError('Config file specified in {0} ({1}) does not exist'.\
            format(CONFIG_ENV, os.environ[CONFIG_ENV]))


config = ConfigParser.RawConfigParser()
config.read(os.environ.get(CONFIG_ENV))

def datastore_location():
    host = config.get('datastore', 'host')
    port = config.getint('datastore', 'port')
    return (host, port,)

def multiplexer_location():
    host = config.get('multiplexer', 'host')
    port = config.getint('multiplexer', 'port')
    return (host, port,)

def webapp_location():
    host = config.get('webapp', 'host')
    port = config.getint('webapp', 'port')
    root = config.get('webapp', 'root_folder') or ''
    return (host, port, root,)

def get_config_filename():
    return os.environ[CONFIG_ENV]

def get_logging_level():
    import logging
    lvl = 'INFO'
    try:
        lvl = config.get('main', 'loglevel')
    except:
        logging.ERROR('No logging level set, defaulting to INFO')
    return getattr(logging, lvl.upper())
