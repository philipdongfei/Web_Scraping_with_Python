import logging
from logging.config import fileConfig

#fileConfig('logging_config.ini')
fileConfig('logging_config.conf')
logger = logging.getLogger()
logger.debug('often makes a very good meal of %s', 'visiting tourists')

