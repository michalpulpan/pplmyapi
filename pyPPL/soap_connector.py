import logging
import requests
import requests.adapters
from abc import (ABC, abstractmethod, )
from datetime import datetime
import xmltodict
import json
import copy

from .soap_actions.login import SOAPActionLogin
from .soap_actions.is_healthy import SOAPActionIsHealthy

from . import conf

logger = logging.getLogger(__name__)

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