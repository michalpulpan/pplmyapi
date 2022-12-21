from ..conf import (Currency, )
from ..validators import (max_length, )
from .base import (SerializableObject, )

class PaymentInfo(SerializableObject):

    xml_mapping = {
        'cod_price': 'CodPrice',
        'cod_currency': 'CodCurrency',
        'cod_vs': 'CodVarSym',
        'insurance_price': 'InsurPrice',
        'insurance_currency': 'InsurCurrency',
        'bank_account': 'BankAccount',
        'bank_code': 'BankCode',
        'iban': 'IBAN',
        'swift': 'Swift',
        'specific_symbol': 'SpecSymbol',
    }

    def __init__(
        self,
        cod_price: float = None,
        cod_currency: str = None,
        cod_vs: str = None,
        insurance_price: float = None,
        insurance_currency: str = None,
        bank_account: str = None,
        bank_code: str = None,
        iban: str = None,
        swift: str = None,
        specific_symbol: str = None,
        ) -> None:

        # cod price and it's currency
        if cod_price is not None and cod_currency is None:
            raise ValueError('COD currency must be provided if COD price is provided')
        self.cod_price = cod_price
        if cod_currency not in Currency.__members__: 
            raise ValueError(f'Currency {cod_currency} is not supported')
        self.cod_currency = cod_currency
        
        if not cod_vs and cod_price:
            raise ValueError('COD VS must be provided if COD price is provided')

        self.cod_vs = max_length(cod_vs, 30)
        
        # insurance price and it's currency
        if insurance_price is not None and insurance_currency is None:
            raise ValueError('Insurance currency must be provided if insurance price is provided')
        self.insurance_price = insurance_price
        if insurance_currency not in Currency.__members__:
            raise ValueError(f'Currency {insurance_currency} is not supported')
        self.insurance_currency = insurance_currency

        # bank account and bank code
        if bank_account is not None and bank_code is None:
            raise ValueError('Bank code must be provided if bank account is provided')
        if bank_account is None and bank_code is not None:
            raise ValueError('Bank account must be provided if bank code is provided')
        self.bank_account = max_length(bank_account, 10)
        self.bank_code = max_length(bank_code, 4)
        if (iban or swift) and (self.bank_account or self.bank_code):
            raise ValueError('Bank account and bank code cannot be provided if IBAN or SWIFT is provided and vice versa')
        
        if iban and not swift:
            raise ValueError('SWIFT must be provided if IBAN is provided')
        if swift and not iban:
            raise ValueError('IBAN must be provided if SWIFT is provided')

        self.iban = max_length(iban, 50)
        self.swift = max_length(swift, 50)

    