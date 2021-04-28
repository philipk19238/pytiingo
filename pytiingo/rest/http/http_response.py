import json
import pandas as pd

from io import StringIO
from typing import List, Dict
from pydantic import BaseModel
from requests import Response
from pandas import DataFrame


class HttpResponse(BaseModel):

    status_code: int
    reason_phrase: str
    text: str
    request: Response

    def is_success(self) -> bool:
        return 200 <= self.status_code < 300

    def to_json(self) -> List[Dict]:
        return json.loads(self.text)

    def to_pandas(self) -> DataFrame:
        return pd.read_csv(StringIO(self.text), sep=',')
