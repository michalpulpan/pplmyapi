from ..base import (SOAPAction)

import xmltodict
import logging
from ... import conf


logger = logging.getLogger(__name__)


class SOAPActionLogin(SOAPAction):
    ACTION = 'Login'
    soap_body = """<v1:Login> 
            <v1:Auth>
                <v1:CustId>{}</v1:CustId> 
                <v1:Password>{}</v1:Password> 
                <v1:UserName>{}</v1:UserName>
            </v1:Auth> 
        </v1:Login>"""

    def __init__(self, ) -> None:
        super().__init__()

    def make_soap_body(self) -> str:
        """
        Make SOAP body for Login action
        input data: CustId, Password, UserName into soap_body
        """
        self.data += self.soap_body.format(
            conf.SOAP_CUST_ID,
            conf.SOAP_PASSWORD,
            conf.SOAP_USERNAME,
        )

    def parse_success_response(self, response: str) -> object:
        """
        Parse response from SOAP API and return object

        """
        response_object = xmltodict.parse(response)
        return {'token': response_object['LoginResponse']['LoginResult']['AuthToken']}

