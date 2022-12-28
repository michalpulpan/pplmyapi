from ..conf import (Currency, )
from ..validators import (max_length, )
from .base import (SerializableObject, SerializerField, )

class SpecialDelivery(SerializableObject):

    xml_mapping = {
        'parcel_shop_code': SerializerField('v1:ParcelShopCode'),
    }

    parcel_shop_code: str = None

    def __init__(
        self,
        parcel_shop_code: str,
        ) -> None:

        self.parcel_shop_code = max_length(parcel_shop_code, 50)