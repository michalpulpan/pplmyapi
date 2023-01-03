from pyPPL.conf import Product, ExternalNumber, Flag, Services
from pyPPL.models.package_flag import PackageFlag
from pyPPL.models.package_service import PackageService
from pyPPL.models.payment_info import PaymentInfo
from pyPPL.models.recipient import Recipient
from pyPPL.models.special_delivery import SpecialDelivery
from pyPPL.models.weighted_package_info import WeightedPackageInfo
from pyPPL.models.package_external_number import PackageExternalNumber
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
# con.login()
# check health
# con.is_healty()
# get version
# con.version()


# create packages
package = Package(
    package_number="123456789",
    package_product_type=Product.PPL_PARCEL_CZ_SMART_COD,
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
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    special_delivery=SpecialDelivery(
        parcel_shop_code='123456789',
    ),
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
            code=Services.COD,
        )
    ]
)

# print(package.to_xml())

# create packages
packages = [package]

con.create_packages(packages)

# import requests
# xml_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://myapi.ppl.cz/v1"> 
#         <soapenv:Header/>
#         <soapenv:Body><v1:CreatePackages> 
#         <v1:Auth>
#             <v1:AuthToken>eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJiN19YUXZWZ2dDWDg1YXcwYV9XV3ZCa1pXOXNmaC13MkF1UkNYS0t6M1lzIn0.eyJleHAiOjE2NzI3NTAwNTQsImlhdCI6MTY3Mjc0ODI1NCwianRpIjoiNDYyNjY1ZmMtNmZjZS00YTJkLTgwMDktYTIwMDJkZjgxMmY3IiwiaXNzIjoiaHR0cHM6Ly9hdXRoc2VydmljZS1wcm9kLnBwbC5jei9hdXRoL3JlYWxtcy9ydG1fY3pfbXlhcGkiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiNjBiNmY5YjktYWQzMC00YjAxLWFhYWUtYzIxNTU4ODI2OTlhIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiTXlBcGlDbGllbnQiLCJzZXNzaW9uX3N0YXRlIjoiYzMxZmQ5MzItZTcwOC00ZGMyLWE0MGMtZWJlZmRlZjVkNmE0IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJkZWZhdWx0LXJvbGVzLXJ0bV9jel9teWFwaSIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJteWFwaS51c2VyIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYzMxZmQ5MzItZTcwOC00ZGMyLWE0MGMtZWJlZmRlZjVkNmE0IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImVwcyI6eyJkZXBvdCI6eyJpZCI6MTN9LCJjdXN0b21lciI6eyJpZCI6MjA1MDkzN319LCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJoZGs1NTg3NDUifQ.kbpNrnNYAw3XXhm5meaCKaOA0CMbPjC5nncXbvFeqBzGfKf55vnfaxP1vI1x5Y_OcolRF1c_d6wlCDb4Wnat7hGlvpoGkbCkH3JIOs92baj_IoqTqOapvTYqAdZ9z9ih6D8Q9GVoMcXVWKzX4WWmbkoa63PDXlsuEBxjWL9B1Ju2N3ilqcSemBvGCCjpMMXPYefgNv5qgT0NYv8b5USa39AWsm1yINXb_R2z6K1g0dReSCPCqEewGIgWCOSAZ0V2GzxYl2YvAgyMWWbsr1ShE1fGPG8swd3YrljEa_gkNm8Gwrv9SMYiA9GLa-JtviPXMCUmReTZ9r_hC3kp64c4yg</v1:AuthToken> 
#         </v1:Auth>
#         <v1:Packages>
#                 <v1:MyApiPackageIn><v1:PackNumber>123456789</v1:PackNumber><v1:PackProductType>SMARD</v1:PackProductType><v1:Note>test</v1:Note><v1:Recipient>
#         <v1:City>Hradec Králové</v1:City>
#         <v1:Country>CZ</v1:Country>
#         <v1:Email>j.doe@example.com</v1:Email>
#         <v1:Name>John Doe</v1:Name>
#         <v1:Phone>123456789</v1:Phone>
#         <v1:Street>Hlavní 1</v1:Street>
#         <v1:ZipCode>500 01</v1:ZipCode>
# </v1:Recipient><v1:SpecialDelivery>
#         <v1:ParcelShopCode>123456789</v1:ParcelShopCode>
# </v1:SpecialDelivery><v1:PaymentInfo>
#         <v1:BankAccount>123456789</v1:BankAccount>
#         <v1:BankCode>0300</v1:BankCode>
#         <v1:CodCurrency>CZK</v1:CodCurrency>
#         <v1:CodPrice>100</v1:CodPrice>
#         <v1:CodVarSym>123456789</v1:CodVarSym>
#         <v1:InsurCurrency>CZK</v1:InsurCurrency>
#         <v1:InsurPrice>100</v1:InsurPrice>
#         <v1:SpecSymbol>123456789</v1:SpecSymbol>
# </v1:PaymentInfo><v1:PackagesExtNums>
#         <v1:MyApiPackageExtNum>
#                 <v1:Code>B2CO</v1:Code>
#                 <v1:ExtNumber>123456789</v1:ExtNumber>
#         </v1:MyApiPackageExtNum>
#         <v1:MyApiPackageExtNum>
#                 <v1:Code>CUST</v1:Code>
#                 <v1:ExtNumber>123456789</v1:ExtNumber>
#         </v1:MyApiPackageExtNum>
# </v1:PackagesExtNums><v1:PackageServices>
#         <v1:MyApiPackageInServices>
#                 <v1:SvcCode>COD</v1:SvcCode>
#         </v1:MyApiPackageInServices>
# </v1:PackageServices><v1:PackageFlags>
#         <v1:MyApiFlag>
#                 <v1:Code>CL</v1:Code>
#                 <v1:Value>true</v1:Value>
#         </v1:MyApiFlag>
# </v1:PackageFlags><v1:PackageSet>
#         <v1:MastepackNumber>123456789</v1:MastepackNumber>
#         <v1:PackageInSetNr>1</v1:PackageInSetNr>
#         <v1:PackagesInSet>1</v1:PackagesInSet>
# </v1:PackageSet><v1:WeightedPackageInfo>
#         <v1:Weight>10.22</v1:Weight>
# </v1:WeightedPackageInfo></v1:MyApiPackageIn>
#             </v1:Packages>
#     </v1:CreatePackages></soapenv:Body>
#         </soapenv:Envelope>"""


# import xml.dom.minidom
# temp = xml.dom.minidom.parseString(xml_data)
# new_xml = temp.toprettyxml()
# print(new_xml)

# from lxml import etree
# xmlRootNode = etree.fromstring(xml_data)
# new_xml = etree.tostring(xmlRootNode, xml_declaration=False, encoding="UTF-8", pretty_print=True)
# print(new_xml)
# element = ET.XML(data)
# data = ET.tostring(element, encoding='utf8')



# response = requests.post(
#     'https://myapi.ppl.cz/MyApi.svc',
#     data=new_xml,
#     headers={'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': 'http://myapi.ppl.cz/v1/IMyApi2/CreatePackages'},
#     timeout=10,
# )


# print(response.text)
# print(response.request.headers)