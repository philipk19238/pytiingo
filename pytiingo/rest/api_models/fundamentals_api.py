from pytiingo.rest.api_models.base_api import BaseApi as base


class FundamentalsApi(base):

    @base.format_output
    @base.execute_request
    def get_definitions(self, **params):
        _query_url = '/tiingo/fundamentals/definitions'
        _query_parameters = {
            'tickers': params.get('tickers'),
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_statements(self, ticker: str, **params):
        _query_url = f'/tiingo/fundamentals/{ticker}/statements'
        _query_parameters = {
            'asReported': params.get('asReported'),
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'sort': params.get('sort')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_daily_metrics(self, ticker: str, **params):
        _query_url = f'/tiingo/fundamentals/{ticker}/daily'
        _query_parameters = {
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'sort': params.get('sort')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def get_metadata(self, **params):
        _query_url = '/tiingo/fundamentals/meta'
        _query_parameters = {
            'tickers': params.get('tickers')
        }
        return _query_url, _query_parameters
