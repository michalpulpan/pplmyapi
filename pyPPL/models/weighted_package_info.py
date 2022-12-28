from ..conf import (Currency, )
from ..validators import (max_length, )
from .base import (SerializableObject, )

class WeightedPackageInfo(SerializableObject):

    xml_mapping = {
        'weight': 'v1:Weight',
    }

    weight: float = None

    def __init__(
        self,
        weight: float,
        ) -> None:

        # cod price and it's currency
        if weight is None:
            raise ValueError('Weight must be provided')
        self.weight = weight
        