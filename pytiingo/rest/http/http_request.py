from pydantic import BaseModel
from typing import Dict


class HttpRequest(BaseModel):

    http_method: str
    query_url: str
    headers: Dict = None
    query_parameters: Dict = None
    proxies: Dict = None
