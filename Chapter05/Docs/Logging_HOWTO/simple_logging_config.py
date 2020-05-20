import logging
from logging.config import fileConfig
from os import path

#logpath = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logpath='logging.conf'
#logpath='logging_config.ini'
print(logpath)
fileConfig(logpath)

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
