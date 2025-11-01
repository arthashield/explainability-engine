from typing import List, Callable, Dict
from app.compliance.rbi_rules import apply_rbi_rules
from app.compliance.sebi_rules import apply_sebi_rules
from app.compliance.gdpr_rules import apply_gdpr_rules
from app.compliance.internal_sop import apply_internal_sop_rules

POLICY_REGISTRY: Dict[str, List[Callable]] = {
    "RBI": [apply_rbi_rules],
    "SEBI": [apply_sebi_rules],
    "GDPR": [apply_gdpr_rules],
    "INTERNAL_SOP": [apply_internal_sop_rules],
}

def evaluate_policies(data: dict, trace: list, active_policies: List[str]):
    trace.append(f"Active policies: {active_policies}")
    for policy in active_policies:
        rule_functions = POLICY_REGISTRY.get(policy, [])
        for rule_fn in rule_functions:
            result = rule_fn(data, trace)
            trace.append(f"Result from {rule_fn.__name__}: {result}")
    return trace
