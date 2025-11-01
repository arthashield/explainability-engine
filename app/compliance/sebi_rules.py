def apply_sebi_rules(data, trace):
    trace.append("[SEBI] Evaluating SEBI compliance rules...")
    if data.get("security_type") == "INSIDER":
        trace.append("[SEBI] Rule Trigger: Insider-related transaction")
        return "SEBI_FLAGGED"
    return "SEBI_CLEAR"
