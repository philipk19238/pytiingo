import os

from typing import Dict
from dotenv import load_dotenv, find_dotenv
from pytiingo.rest.utils import cached_property
from pytiingo.rest.http.http_client import HttpClient

load_dotenv(find_dotenv())


class Configuration(object):

    TIINGO_BASE = 'https://api.tiingo.com'

    def __init__(self, token: str = None,
                 output_format: str = 'json',
                 proxy: Dict = None):
        self._check_init_parameters(token, output_format)
        self._token = token or os.getenv('TIINGO_API_TOKEN')
        self._proxy = proxy or {}
        self._output_format = output_format

    @property
    def token(self) -> str:
        return self._token

    @property
    def proxy(self) -> Dict:
        return self._proxy

    @property
    def output_format(self) -> str:
        return self._output_format

    @cached_property
    def http_client(self) -> HttpClient:
        return HttpClient()

    @property
    def base_uri(self) -> str:
        return self.TIINGO_BASE

    @property
    def headers(self) -> Dict:
        return {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }

    def _check_init_parameters(self, token: str, output_format: str) -> None:
        if token is None:
            token = os.getenv('TIINGO_API_TOKEN')
        if not token or not isinstance(token, str):
            raise ValueError("""
                             The Tiingo API Key must be provided
                             either through the token parameter
                             or through the environmental variable
                             TIINGO_API_TOKEN. Get a free key from the
                             Tiingo website:
                             https://api.tiingo.com
                             """)
        if output_format.lower() not in ['json', 'pandas']:
            raise ValueError('Output format must be either "json" or "pandas"')
