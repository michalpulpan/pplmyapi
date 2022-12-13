import logging
import requests
import requests.adapters
from abc import (ABC, abstractmethod, )
from datetime import datetime
import xmltodict
import json
import copy

from . import conf

logger = logging.getLogger(__name__)

class SOAPAction(ABC):
    ACTION = None
    HEADERS = None
    URL = conf.SOAP_API_URL
    data = ''
    soap_body = None

    def __init__(self) -> None:
        
        self.HEADERS = copy.deepcopy(conf.SOAP_HEADERS) # copy headers to avoid changing original headers in conf
        
        if self.ACTION is None:
            raise NotImplementedError('SOAPAction.ACTION must be set')
        self.HEADERS['SOAPAction'] =  f"{self.HEADERS['SOAPAction']}{self.ACTION}" # add action to SOAPAction header

    def header(self) -> None:
        """
        Make SOAP header                        
        """
        self.data += f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://myapi.ppl.cz/v1"> 
        <soapenv:Header/>
        <soapenv:Body>
        """
    def footer(self) -> None:
        """
        Make SOAP footer
        """
        self.data += f"""</soapenv:Body>
        </soapenv:Envelope>"""

    def make_data(self) -> str:
        """
        Make SOAP text/xml data from header, body and footer for request
        """
        self.header()
        self.make_soap_body()
        self.footer()
        return self.data

    @abstractmethod
    def make_soap_body(self) -> str:
        """
        Make SOAP body from self.soap_body with possibly some variables embedded
        """
        raise NotImplementedError('make_soap_body must be implemented')

    @abstractmethod
    def parse_success_response(self, response: str) -> object:
        """
        Parse success response from SOAP API and return object
        """
        raise NotImplementedError('parse_response must be implemented')

    def parse_error_response(self, response: str) -> object:
        """
        Parse generic error response from SOAP API and return object

        """
        response_object = json.dumps(xmltodict.parse(response))
        return {'code': response_object['s:Fault'], 'message': response_object['s:Fault']['faultstring']}
    
    def get_body(self, response: str) -> str:
        """
        Get SOAP body from response
        """
        return response.split('<s:Body>')[1].split('</s:Body>')[0]

    def __call__(self) -> object:
        """
        Call SOAP action
        """

        if self.soap_body is None:
            raise ValueError('data must be set')
        
        self.make_data()

        logging.debug(f"Calling SOAP action {self.ACTION} with data: {self.data}")
        response = requests.post(
            self.URL,
            data=self.data,
            headers=self.HEADERS,
            timeout=10,
        )
        if response.status_code != 200:
            # raise Exception(f"SOAP API returned status code {response.status_code}")
            logging.error(f"SOAP API returned status code {response.status_code}")
            logging.error(f"SOAP API returned status code {response.text}")
            response_body = self.parse_error_response(
                self.get_body(response.text)
            )
            logging.error(f"JSON response body: {response_body}")
            return response_body

        logging.debug(f"SOAP response: {response.text}")
        response_body = self.parse_success_response(
            self.get_body(response.text)
        )
        logging.debug(f"JSON response body: {response_body}")
        return response_body

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


class SOAPActionIsHealthy(SOAPAction):
    ACTION = 'IsHealtly'
    soap_body = """<v1:IsHealtly/>"""

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



class SOAPConnector:
    AUTH_TOKEN = None
    AUTH_TOKEN_TIMESTAMP = None
    AUTH_TOKEN_MAX_AGE = conf.SOAP_AUTH_TOKEN_MAX_AGE


    def __init__(self) -> None:
        pass

    def call():
        pass

    def is_healty(self) -> bool:
        is_healty = SOAPActionIsHealthy()
        response = is_healty()
        if 'healthy' in response and response['healthy'] == 'Healthy':
            return True
        return False
            


    def login(self) -> bool:

        if self.AUTH_TOKEN is not None:
            if datetime.now().timestamp() - self.AUTH_TOKEN_TIMESTAMP < self.AUTH_TOKEN_MAX_AGE:
                return True

        login = SOAPActionLogin()
        response = login()
        if 'token' in response:
            self.AUTH_TOKEN = response['token']
            self.AUTH_TOKEN_TIMESTAMP = datetime.now().timestamp()
            return True
        return False