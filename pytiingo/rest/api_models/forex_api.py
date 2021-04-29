from pytiingo.rest.api_models.base_api import BaseApi as base


class ForexApi(base):

    @base.format_output
    @base.execute_request
    def get_multiple_top_of_book(self, **params):
        _query_url = '/tiingo/fx/top'
        _query_parameters = {
            'tickers': params.get('tickers')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_one_top_of_book(self, ticker: str, **params):
        _query_url = f'/tiingo/fx/{ticker}/top'
        _query_parameters = {}
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_prices(self, ticker: str, **params):
        _query_url = f'/tiingo/fx/{ticker}/prices'
        _query_parameters = {
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'resampleFreq': params.get('resampleFreq')
        }
        return _query_url, _query_parameters
