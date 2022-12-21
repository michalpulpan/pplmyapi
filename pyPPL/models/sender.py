from ..conf import (Country, )
from ..validators import (max_length, )
from .base import (SerializableObject, )

class Sender(SerializableObject):

    xml_mapping = {
        'name': 'Name',
        'city': 'City',
        'street': 'Street',
        'zip_code': 'ZipCode',
        'country': 'Country',
        'phone': 'Phone',
        'email': 'Email',
        'contact': 'Contact',
        'name2': 'Name2',
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
        
        self.name = max_length(name, 250)
        self.city = max_length(city, 50)
        self.street = max_length(street, 50)
        self.zip_code = max_length(zip_code, 10)

        if country not in Country.__members__: 
            raise ValueError(f'Country {country} is not supported')
        self.country = country

        self.phone = max_length(phone, 30)
        self.email = max_length(email, 50)
        self.contact = max_length(contact, 30)
        self.name2 = max_length(name2, 250)
    

    