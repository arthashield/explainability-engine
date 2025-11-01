from fastapi import APIRouter
from app.api.schemas import ExplainRequest, ExplainResponse
from app.core.trace_logger import store_audit_trace
from app.agents.compliance_agent import run_compliance_checks

router = APIRouter()

@router.post("/explain", response_model=ExplainResponse)
def explain(payload: ExplainRequest):
    trace = run_compliance_checks(payload.data)
    store_audit_trace(trace)
    return ExplainResponse(trace=trace)
