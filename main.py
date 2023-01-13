from pyPPL.conf import Product, ExternalNumber, Flag, Services
from pyPPL.models import (
    Dormant,
    PackageFlag,
    PackageService,
    PaymentInfo,
    Recipient,
    Sender,
    SpecialDelivery,
    WeightedPackageInfo,
    PackageExternalNumber,
    Package,
)
from pyPPL.ppl import PPL
import logging.config
from datetime import datetime
from os import path
import os


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
ppl = PPL(
    rest_client_id=os.getenv('REST_CLIENT_ID'),
    rest_client_secret=os.getenv('REST_CLIENT_SECRET'),
    soap_customer_id=os.getenv('SOAP_CUST_ID'),
    soap_username=os.getenv('SOAP_USERNAME'),
    soap_password=os.getenv('SOAP_PASSWORD'),
)
con = ppl.soap_connector()
# login 
con.login()
# check health
con.is_healty()
# get version
con.version()


# create packages
package = Package(
    package_number="123456789",
    package_product_type=Product.PPL_PARCEL_CZ_PRIVATE_COD,
    note = "test",
    recipient=Recipient(
        name="John Doe",
        city="Hradec Králové",
        street="Hlavní 1",
        zip_code="50001",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    sender=Sender(
        name="Milpex s.r.o.",
        street="Piletická 55/36",
        city="Hradec Králové",
        zip_code="50003",
        country="CZ",
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456',
        bank_account='123456789',
        bank_code='0300'
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    # special_delivery=SpecialDelivery(
    #     parcel_shop_code='123456789',
    # ),
    # external_numbers=[
    #     PackageExternalNumber(
    #         external_number='123456789',
    #         code=ExternalNumber.B2CO
    #     ),
    #     PackageExternalNumber(
    #         external_number='123456789',
    #         code=ExternalNumber.CUST
    #     )
    # ],
    flags=[
        PackageFlag(
            code=Flag.CL,
            value=True
        )
    ],
    # package_services=[
    #     PackageService(
    #         code=Services.COD,
    #     )
    # ],
    # dormant=Dormant(
    #     recipient=Recipient(
    #         name="Milpex s.r.o.",
    #         street="Piletická 55/36",
    #         city="Hradec Králové",
    #         zip_code="50003",
    #         country="CZ",
    #     ),
    #     note="Vratkový štítek k objednávce"
    # )
)

package2 = Package(
    package_number="12345678",
    package_product_type=Product.PPL_PARCEL_CZ_PRIVATE_COD,
    note = "test",
    recipient=Recipient(
        name="Jan Novák",
        city="Hradec Králové",
        street="Hlavní 1",
        zip_code="50001",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    sender=Sender(
        name="Milpex s.r.o.",
        street="Piletická 55/36",
        city="Hradec Králové",
        zip_code="50003",
        country="CZ",
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456',
        bank_account='123456789',
        bank_code='0300'
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    # special_delivery=SpecialDelivery(
    #     parcel_shop_code='123456789',
    # ),
    # external_numbers=[
    #     PackageExternalNumber(
    #         external_number='123456789',
    #         code=ExternalNumber.B2CO
    #     ),
    #     PackageExternalNumber(
    #         external_number='123456789',
    #         code=ExternalNumber.CUST
    #     )
    # ],
    flags=[
        PackageFlag(
            code=Flag.CL,
            value=True
        )
    ],
    # package_services=[
    #     PackageService(
    #         code=Services.COD,
    #     )
    # ],
    # dormant=Dormant(
    #     recipient=Recipient(
    #         name="Milpex s.r.o.",
    #         street="Piletická 55/36",
    #         city="Hradec Králové",
    #         zip_code="50003",
    #         country="CZ",
    #     ),
    #     note="Vratkový štítek k objednávce"
    # )
)


package3 = Package(
    package_number="12445678",
    package_product_type=Product.PPL_PARCEL_CZ_PRIVATE_COD,
    note = "test",
    recipient=Recipient(
        name="Jana Nováková",
        city="Hradec Králové",
        street="Hlavní 1",
        zip_code="50001",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    sender=Sender(
        name="Milpex s.r.o.",
        street="Piletická 55/36",
        city="Hradec Králové",
        zip_code="50003",
        country="CZ",
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456',
        bank_account='123456789',
        bank_code='0300'
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    # special_delivery=SpecialDelivery(
    #     parcel_shop_code='123456789',
    # ),
    external_numbers=[
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.B2CO
        ),
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.CUST
        )
    ],
    flags=[
        PackageFlag(
            code=Flag.CL,
            value=True
        )
    ],
    package_services=[
        PackageService(
            code=Services.DPOD,
        )
    ],
    # dormant=Dormant(
    #     recipient=Recipient(
    #         name="Milpex s.r.o.",
    #         street="Piletická 55/36",
    #         city="Hradec Králové",
    #         zip_code="50003",
    #         country="CZ",
    #     ),
    #     note="Vratkový štítek k objednávce"
    # )
)

con.create_packages(
    packages=[package3],
)


# # create packages
# packages = [package3]

# # create rest_connector
# rest_con = ppl.rest_connector

# # create rest_action
# rest_con.get_labels(
#     packages=packages,
#     file_path = './out_test',
#     file_name = 'test3.pdf',
# )

