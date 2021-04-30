from typing import Dict
from pytiingo.rest.configuration import Configuration
from pytiingo.rest.utils import cached_property

from pytiingo.rest.api_models.crypto_api import CryptoApi
from pytiingo.rest.api_models.eod_api import EndOfDayApi
from pytiingo.rest.api_models.forex_api import ForexApi
from pytiingo.rest.api_models.fundamentals_api import FundamentalsApi
from pytiingo.rest.api_models.iex_api import IEXApi
from pytiingo.rest.api_models.news_api import NewsApi


class RESTClient(object):

    def __init__(self, token: str = None,
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

    @cached_property
    def forex(self):
        return ForexApi(self.config)

    @cached_property
    def fundamentals(self):
        return FundamentalsApi(self.config)

    @cached_property
    def iex(self):
        return IEXApi(self.config)

    @cached_property
    def news(self):
        return NewsApi(self.config)
