from typing import Dict
from pytiingo.rest.configuration import Configuration


class ApiMixin(object):

    def _execute_request(self, query_url: str, query_parameters: Dict):
        request = self.config.http_client.get(
            query_url,
            query_parameters,
            self.config.headers,
            self.config.proxies
        )
        response = self.config.http_client.execute(request)
        return response


class BaseApi(ApiMixin):

    def __init__(self, config: Configuration):
        self._config = config

    @property
    def config(self):
        return self._config

    @classmethod
    def execute_request(cls, func):
        def _execute_request(self, *args, **kwargs):
            query_url, query_parameters = func(self, *args, **kwargs)
            query_url = self.config.base_uri + query_url
            query_parameters['token'] = self.config.token
            response = self._execute_request(query_url, query_parameters)
            return response
        return _execute_request
