from ..base import (SOAPAction)
import xmltodict
import logging


logger = logging.getLogger(__name__)

class SOAPActionCreatePackages(SOAPAction):
    """
    CreatePackages SOAP action
    Action for creating packages with defined tracking number.
    Generaly sending packages to customer.
    """

    ACTION = 'CreatePackages'
    soap_body = """"""

    def __init__(self, ) -> None:
        super().__init__()

    def make_soap_body(self) -> str:
        """
        Make SOAP body for IsHealtly action
        """
        self.data += self.soap_body

    def parse_success_response(self, response: str) -> object:
        """
        Parse response from SOAP API and return object

        """
        response_object = xmltodict.parse(response)
        return {'healthy': response_object['IsHealtlyResponse']['IsHealtlyResult']}
