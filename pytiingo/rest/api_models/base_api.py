from typing import Dict, List, Union
from pandas import DataFrame

from pytiingo.rest.configuration import Configuration
from pytiingo.rest.http.http_response import HttpResponse


class ApiMixin(object):

    def _execute_request(self, query_url: str, query_parameters: Dict) -> HttpResponse:
        request = self.config.http_client.get(
            query_url,
            query_parameters,
            self.config.headers,
            self.config.proxy
        )
        response = self.config.http_client.execute(request)
        return response

    def _format_output(self, response: HttpResponse) -> Union[List[Dict], DataFrame]:
        if not response.is_success():
            return response.return_error()
        if self.config.output_format == 'json':
            return response.to_json()
        else:
            return response.to_pandas()

    def _clean_query_parameters(self, query_parameters: Dict) -> Dict:
        cleaned = {}
        for k, v in query_parameters.items():
            if v:
                if isinstance(v, list):
                    v = ','.join(v)
                cleaned[k] = v
        return cleaned


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
            if self.config.output_format == 'pandas':
                query_parameters['format'] = 'csv'
            else:
                query_parameters['format'] = 'json'
            query_parameters['token'] = self.config.token
            query_parameters = self._clean_query_parameters(query_parameters)
            response = self._execute_request(query_url, query_parameters)
            return response
        return _execute_request
