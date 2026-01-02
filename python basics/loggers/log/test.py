from logger import logging # we created a file logger where we did basic config and imported than from that file like here. and used it.
def add(a,b):

    logging.debug("addition operation is processed:")
    return a+b
logging.debug("addition operation completed:")
print(add(5,7))
 # add when you run it an app log file is created in log folder. before running makesure your path in terminal is same as in log folder than type python test.py