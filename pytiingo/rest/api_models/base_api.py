from typing import Dict, List, Union
from pytiingo.rest.configuration import Configuration
from pytiingo.rest.http.http_response import HttpResponse
from pandas import DataFrame


class ApiMixin(object):

    def _execute_request(self, query_url: str, query_parameters: Dict) -> HttpResponse:
        request = self.config.http_client.get(
            query_url,
            query_parameters,
            self.config.headers,
            self.config.proxies
        )
        response = self.config.http_client.execute(request)
        return response

    def _format_output(self, response: HttpResponse) -> Union[List[Dict], DataFrame]:
        try:
            assert response.is_success() == True
        except AssertionError:
            return response.to_json()
        if self.config.output_format == 'json':
            return response.to_json()
        else:
            return response.to_pandas()


class BaseApi(ApiMixin):

    def __init__(self, config: Configuration):
        self._config = config

    @property
    def config(self):
        return self._config

    @classmethod
    def format_output(cls, func):
        def _format_output(self, *args, **kwargs):
            response = func(self, *args, **kwargs)
            marshalled_output = self._format_output(response)
            return marshalled_output
        return _format_output

    @classmethod
    def execute_request(cls, func):
        def _execute_request(self, *args, **kwargs):
            query_url, query_parameters = func(self, *args, **kwargs)
            query_url = self.config.base_uri + query_url
            query_parameters['token'] = self.config.token
            response = self._execute_request(query_url, query_parameters)
            return response
        return _execute_request
