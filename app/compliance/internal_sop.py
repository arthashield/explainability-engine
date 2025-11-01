def apply_internal_sop_rules(data, trace):
    trace.append("[INTERNAL_SOP] Running internal SOP checks...")
    if data.get("channel") == "MANUAL" and data.get("risk_score", 0) > 7:
        trace.append("[INTERNAL_SOP] Rule Trigger: Manual processing + High risk")
        return "SOP_ESCALATE"
    return "SOP_OK"
