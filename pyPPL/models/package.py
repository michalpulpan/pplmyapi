from ..validators import (max_length, )
from .base import (SerializableObject, )

from .recipient import (Recipient, )
from .sender import (Sender, )
from .payment_info import (PaymentInfo, )

class Package(SerializableObject):

    xml_mapping = {
    }


    def __init__(
        self,
        package_number: str,
        package_product_type: int,
        note: str,
        recipient: Recipient,
        city_routing,
        sender: Sender = None,
        depo_code: str = None,
        special_delivery = None,
        payment_info: PaymentInfo = None,
        external_numbers: list = [],
        package_services: list = [],
        flags: list = [],
        weighted_package_info = None,
        package_set = None
        ) -> None:
        
        # TODO: control if product_type has cash on delivery and payment_info provided
        
        self.note = max_length(note, 300)
        self.package_number = max_length(package_number, 20)
        
        self.sender = sender
        self.recipient = recipient
        self.package_product_type = package_product_type
        
        