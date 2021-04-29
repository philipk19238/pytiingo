from typing import Dict
from pytiingo.rest.configuration import Configuration
from pytiingo.rest.utils import cached_property

from pytiingo.rest.api_models.crypto_api import CryptoApi
from pytiingo.rest.api_models.eod_api import EndOfDayApi


class Client(object):

    def __init__(self, token: str,
                 output_format: str = 'json',
                 proxy: Dict = None,
                 config: Configuration = None):
        if config:
            self.config = config
        else:
            self.config = Configuration(
                token,
                output_format,
                proxy)

    @cached_property
    def crypto(self):
        return CryptoApi(self.config)

    @cached_property
    def eod(self):
        return EndOfDayApi(self.config)
