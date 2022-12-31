from collections import OrderedDict
from ..conf import (Services, )
from ..validators import (max_length, )
from .base import (SerializableObject, SerializerField)

class PackageService(SerializableObject):

    xml_mapping = OrderedDict([
        ('code', SerializerField('v1:SvcCode')),
    ])
    code: str

    def __init__(
        self,
        code: str,
        ) -> None:

        if code not in Services:
            raise ValueError(f'Invalid code: {code} for package services')
        self.code = code.value

        
