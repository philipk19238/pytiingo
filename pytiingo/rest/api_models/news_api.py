from pytiingo.rest.api_models.base_api import BaseApi as base


class NewsApi(base):

    @base.format_output
    @base.execute_request
    def get_news(self, **params):
        _query_url = '/tiingo/news'
        _query_parameters = {
            'tickers': params.get('tickers'),
            'tags': params.get('tags'),
            'source': params.get('source'),
            'startDate': params.get('startDate'),
            'endDate': params.get('endDate'),
            'limit': params.get('limit'),
            'offset': params.get('offset'),
            'sortBy': params.get('sortBy'),
            'onlyWithTickers': params.get('onlyWithTickers')
        }
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def download_news(self, file_id: int, **params):
        _query_url = f'/tiingo/news/bulk_download/{file_id}'
        _query_parameters = {}
        return _query_url, _query_parameters

    @base.format_output
    @base.execute_request
    def list_downloadable_news(self, **params):
        _query_url = '/tiingo/news/bulk_download'
        _query_parameters = {}
        return _query_url, _query_parameters
