import json

from pydantic import BaseModel
from requests import Response


class HttpResponse(BaseModel):

    status_code: int
    reason_phrase: str
    text: str
    request: Response

    def is_success(self) -> bool:
        return 200 <= self.status_code < 300
