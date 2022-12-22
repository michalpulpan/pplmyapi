from ..conf import (Country, )
from ..validators import (max_length, )
from .base import (SerializableObject, )

class Recipient(SerializableObject):

    xml_mapping = {
        'name': 'v1:Name',
        'city': 'v1:City',
        'street': 'v1:Street',
        'zip_code': 'v1:ZipCode',
        'country': 'v1:Country',
        'phone': 'v1:Phone',
        'email': 'v1:Email',
        'contact': 'v1:Contact',
        'name2': 'v1:Name2',
    }

    def __init__(
        self,
        name: str,
        city: str,
        street: str,
        zip_code: str,
        country = Country.CZ,
        phone: str = None,
        email: str = None,
        contact: str = None,
        name2: str = None,
        ) -> None:
        
        self.name = max_length(name, 50)
        self.city = max_length(city, 50)
        self.street = max_length(street, 50)
        self.zip_code = max_length(zip_code, 10)

        if not Country.has_value(country): 
            raise ValueError(f'Country {country} is not supported')
        self.country = country

        self.phone = max_length(phone, 30)
        self.email = max_length(email, 50)
        self.contact = max_length(contact, 300)
        self.name2 = max_length(name2, 50)
    

    