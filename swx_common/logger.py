import logging as logg

from .configuration import (get_config_filename, get_logging_level)

logg.basicConfig(filename=get_config_filename(),
                 level=get_logging_level())


def get_logger(name):
    return logg.getLogger(name)

