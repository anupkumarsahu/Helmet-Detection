from helmet.logger import logging
from helmet.exception import HelmetException
import sys

logging.info("Welcome to this project")

try:
    a = 2 + '3'
except Exception as e:
    raise HelmetException(e, sys) from e
