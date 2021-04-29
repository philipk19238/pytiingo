import requests

from typing import Dict
from requests import Response
from pytiingo.rest.http.http_request import HttpRequest
from pytiingo.rest.http.http_response import HttpResponse


class HttpClient(object):

    def __init__(self):
        self.session = requests.session()

    def execute(self, request: HttpRequest):
        response = self.session.request(
            request.http_method,
            request.query_url,
            headers=request.headers,
            params=request.query_parameters,
            proxies=request.proxies)

        return self.convert_response(response)

    def get(self, query_url: str,
            query_parameters: Dict = {},
            headers: Dict = {},
            proxies: Dict = {}) -> HttpRequest:

        return HttpRequest(
            http_method="GET",
            query_url=query_url,
            header=headers,
            query_parameters=query_parameters,
            proxies=proxies)

    def post(self, *args, **kwargs):
        raise NotImplementedError("Method not implemented!")

    def put(self, *args, **kwargs):
        raise NotImplementedError("Method not implemented!")

    def patch(self, *args, **kwargs):
        raise NotImplementedError("Method not implemented!")

    def delete(self, *args, **kwargs):
        raise NotImplementedError("Method not implemented!")

    def convert_response(self, response: Response) -> HttpResponse:
        return HttpResponse(
            status_code=response.status_code,
            reason_phrase=response.reason,
            text=response.text,
            request=response)
