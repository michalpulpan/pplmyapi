from ..conf import (Currency, )
from ..validators import (max_length, )
from .base import (SerializableObject, )

class PackageSet(SerializableObject):

    xml_mapping = {
        'master_number': 'v1:MastepackNumber',
        'current_number_in_set': 'v1:PackageInSetNr',
        'total_packages': 'v1:PackagesInSet',
    }

    master_number: str = None
    current_number_in_set: int = 1
    total_packages: int = 1

    def __init__(
        self,
        master_number: str,
        current_number_in_set: int = 1,
        total_packages: int = 1,
        ) -> None:

        if current_number_in_set > total_packages:
            raise ValueError('Current number in set cannot be greater than total packages')

        self.current_number_in_set = current_number_in_set
        self.total_packages = total_packages
        self.master_number = master_number
        