def apply_rbi_rules(data, trace):
    trace.append("[RBI] Evaluating RBI compliance rules...")
    if data.get("amount", 0) > 50000:
        trace.append("[RBI] Rule Trigger: High-value transaction threshold exceeded")
        return "RBI_FLAGGED"
    return "RBI_CLEAR"
