# Demonstrate logging
# Attributes you can put in the basicConfig:
# level
# filename
# filemode
# format
#      %(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)d
#      s -string, d - number

import logging

# logging.basicConfig(level=logging.WARN) # set the logging level to DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(filename="./mainlog.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s- %(lineno)d")

# prog does stuff
logging.debug("we are doing stuff") # it's like print
logging.info("this is information")
logging.warning("ooooohhh I am not certain about this")
logging.error("not good")
logging.critical("really bad")


