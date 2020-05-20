import logging
import argparse



p = argparse.ArgumentParser()
p.add_argument("--log")

args = p.parse_args()
loglevel = args.log
print('loglevel: ',  loglevel)

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug

numeric_level = getattr(logging, loglevel.upper(), None)
print('numeric_level: ', numeric_level)

if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
logging.basicConfig(filename='setloglevel.log', level=numeric_level)
#logging.basicConfig(filename='setloglevel.log', filemod='w', level=numeric_level) # start afresh

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

