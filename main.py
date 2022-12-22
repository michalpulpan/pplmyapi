from pyPPL.models.payment_info import PaymentInfo
from pyPPL.models.recipient import Recipient
from pyPPL.soap_connector import SOAPConnector
import logging.config
from datetime import datetime
from os import path
from pyPPL.models.package import Package

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
# get version
con.version()


# create packages
package = Package(
    package_number="123456789",
    package_product_type='BUSS',
    note = "test",
    recipient=Recipient(
        name="John Doe",
        city="Hradec Králové",
        street="Hlavní 1",
        zip_code="500 01",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456789',
        bank_account='123456789',
        bank_code='0300'
    )
)

print(package.to_xml())
