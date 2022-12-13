from pyPPL.soap_connector import SOAPConnector
import logging.config
from datetime import datetime
from os import path

CONFIG_DIR = "./config"
LOG_DIR = "./logs"


def setup_logging():
    """Load logging configuration"""
    timestamp = datetime.now().strftime("%Y%m%d-%H:%M:%S")

    logging.config.fileConfig(
        path.abspath(f"{CONFIG_DIR}/logging.dev.ini"),
        disable_existing_loggers=False,
        defaults={"logfilename": f"{LOG_DIR}/{timestamp}.log"},
    )

setup_logging()

# login = SOAPActionLogin()
# login()
con = SOAPConnector()
# login 
con.login()
# check health
con.is_healty()
