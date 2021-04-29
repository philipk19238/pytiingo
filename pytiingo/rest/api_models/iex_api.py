from pytiingo.rest.api_models.base_api import BaseApi as base


class IEXApi(base):

    @base.format_output
    @base.execute_request
    def get_all_top_of_book(self, **params):
        _query_url = '/iex'
        _query_parameters = {}
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_top_of_book(self, ticker: str, **params):
        _query_url = f'/iex/{ticker}'
        _query_parameters = {}
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_prices(self, ticker: str, **params):
        _query_url = f'/iex/{ticker}/prices'
        _query_parameters = {
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'resampleFreq': params.get('resampleFreq'),
            'afterHours': params.get('afterHours'),
            'forceFill': params.get('forceFill')
        }
        return _query_url, _query_parameters
