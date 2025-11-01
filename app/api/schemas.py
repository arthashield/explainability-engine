from pydantic import BaseModel
from typing import Any, List

class ExplainRequest(BaseModel):
    data: Any

class ExplainResponse(BaseModel):
    trace: List[str]
