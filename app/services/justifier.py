
from typing import List
from app.core.llm import generate_justification

def justify_trace(trace: List[str]) -> str:
    return generate_justification(trace)
