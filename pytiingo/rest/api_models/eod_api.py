from pytiingo.rest.api_models.base_api import BaseApi as base


class EndOfDayApi(base):

    @base.format_output
    @base.execute_request
    def get_prices(self, ticker: str, **params):
        _query_url = f'/tiingo/daily/{ticker}/prices'
        _query_parameters = {
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'resampleFreq': params.get('resampleFreq'),
            'sort': params.get('sort'),
            'columns': params.get('columns')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_metadata(self, ticker: str):
        _query_url = f'/tiingo/daily/{ticker}'
        _query_parameters = {}
        return _query_url, _query_parameters
