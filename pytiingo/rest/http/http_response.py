import json
import pandas as pd

from io import StringIO
from typing import List, Dict
from pydantic import BaseModel
from requests import Response
from pandas import DataFrame


class HttpResponse(BaseModel):

    class Config:
        arbitrary_types_allowed = True

    status_code: int
    reason_phrase: str
    text: str
    request: Response

    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    def to_json(self) -> List[Dict]:
        return json.loads(self.text)

    def to_pandas(self) -> DataFrame:
        if self.content_type == 'csv':
            return pd.read_csv(StringIO(self.text), sep=',')
        else:
            return pd.DataFrame.from_dict(self.to_json())

    def return_error(self):
        if self.text:
            detail = self.to_json()['detail']
        else:
            detail = 'No return given from Api'
        error_message = f"""
            Status Code: {self.status_code}\n
            Reason Phrase: {self.reason_phrase}\n
            Error Details: {detail}
        """
        raise ValueError(error_message)

    @property
    def content_type(self):
        if self.text.startswith('[') and self.text.endswith(']'):
            return 'json'
        else:
            return 'csv'
