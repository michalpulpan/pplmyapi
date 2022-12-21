from ..base import (SOAPAction)
import xmltodict
import logging


logger = logging.getLogger(__name__)

class SOAPActionGetPackages(SOAPAction):
    """
    GetPackages SOAP action
    Action for obtaining package detail and it's status.
    """

    ACTION = 'GetPackages'
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
