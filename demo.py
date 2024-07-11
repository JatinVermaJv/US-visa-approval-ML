from us_visa.logger import logging
from us_visa.exception import USvisaException



logging.info("checking log")
try:
    a = 2/10
except Exception as e:
    raise USvisaException(e, sys)    