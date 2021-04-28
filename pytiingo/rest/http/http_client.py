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
            headers: Dict = {},
            query_parameters: Dict = {},
            proxies: Dict = {}) -> HttpRequest:

        return HttpRequest(
            "GET",
            query_url,
            headers,
            query_parameters,
            proxies)

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
            response.status_code,
            response.reason,
            response.text,
            response)
