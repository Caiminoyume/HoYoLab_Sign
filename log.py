import logging

LOG_FORMAT = "%(asctime)s - %(levelname)-8s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S "
logging.basicConfig(filename='sign.log',
                    filemode='w',
                    level=logging.INFO,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT,
                    encoding='utf-8')
log = logging
