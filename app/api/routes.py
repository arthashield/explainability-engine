from fastapi import APIRouter
from app.api.schemas import ExplainRequest, ExplainResponse
from app.core.trace_logger import store_audit_trace
from app.agents.compliance_agent import run_compliance_checks
from app.services.justifier import justify_trace

router = APIRouter()

@router.post("/explain", response_model=ExplainResponse)
def explain(payload: ExplainRequest):
    trace = run_compliance_checks(payload.data)
    # store immutable audit trace to MinIO (if configured)
    try:
        store_audit_trace(trace)
    except Exception:
        # intentionally ignore storage failures in MVP to not block response
        pass
    nl = justify_trace(trace)
    return ExplainResponse(trace=trace, nl_justification=nl)

