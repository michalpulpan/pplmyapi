from ..validators import (max_length, )
from .base import (SerializableObject, )
from ..conf import (Product, )

from .recipient import (Recipient, )
from .sender import (Sender, )
from .payment_info import (PaymentInfo, )

class Package(SerializableObject):

    xml_mapping = {
        'package_number': 'v1:PackNumber',
        'package_product_type': 'v1:PackProductType',
        'note': 'v1:Note',
        'sender': 'v1:Sender',
        'recipient': 'v1:Recipient',
        'depo_code': 'v1:DepoCode',
        'special_delivery': 'v1:SpecialDelivery',
        'payment_info': 'v1:PaymentInfo',
        'external_numbers': 'v1:PackagesExtNums',
        'package_services': 'v1:PackageServices',
        'weighted_package_info': 'v1:WeightedPackageInfo',
        'package_set': 'v1:PackageSet',
        

    }

    package_number: str = None
    package_product_type: str = None
    note: str = None
    sender: Sender = None
    recipient: Recipient = None
    depo_code: str = None
    special_delivery = None
    payment_info: PaymentInfo = None
    external_numbers: list = []
    package_services: list = []
    flags: list = []
    weighted_package_info = None
    package_set = None


    def __init__(
        self,
        package_number: str,
        package_product_type: str,
        note: str,
        recipient: Recipient,
        sender: Sender = None,
        depo_code: str = None,
        special_delivery = None, # TODO: Type
        payment_info: PaymentInfo = None, 
        external_numbers: list = [],  # TODO: Type
        package_services: list = [], # TODO: Type
        flags: list = [], # TODO: Type
        weighted_package_info = None, # TODO: Type
        package_set = None # TODO: Type
        ) -> None:
        
        # TODO: control if product_type has cash on delivery and payment_info provided
        
        self.note = max_length(note, 300)
        self.package_number = max_length(package_number, 20)
        
        self.sender = sender
        self.recipient = recipient
        
        if not Product.has_value(package_product_type):
            raise ValueError(f'Product {package_product_type} is not supported')
        self.package_product_type = package_product_type
        
        self.depo_code = max_length(depo_code, 10)
        self.special_delivery = special_delivery
        self.payment_info = payment_info
        self.external_numbers = external_numbers
        self.package_services = package_services
        self.flags = flags
        self.weighted_package_info = weighted_package_info
        self.package_set = package_set