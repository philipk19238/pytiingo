from pytiingo.rest.api_models.base_api import BaseApi as base


class CryptoApi(base):

    @base.format_output
    @base.execute_request
    def get_top_of_book(self, tickers: str, **params):
        _query_url = '/tiingo/crypto/top'
        _query_parameters = {
            'tickers': tickers,
            'exchanges': params.get('exchanges'),
            'includeRawExchangeData': params.get('includeRawExchangeData'),
            'convertCurrency': params.get('convertCurrency')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_prices(self, tickers: str, **params):
        _query_url = '/tiingo/crypto/prices'
        _query_parameters = {
            'tickers': tickers,
            'baseCurrency': params.get('baseCurrency'),
            'consolidateBaseCurrency': params.get('consolidateBaseCurrency'),
            'exchanges': params.get('exchanges'),
            'includeRawExchangeData': params.get('includeRawExchangeData'),
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'resampleFreq': params.get('resampleFreq'),
            'convertCurrency': params.get('convertCurrency')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_metadata(self, **params):
        _query_url = '/tiingo/crypto'
        _query_parameters = {
            'tickers': params.get('tickers')
        }
        return _query_url, _query_parameters
