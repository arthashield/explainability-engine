def evaluate_rules(data, trace):
    trace.append("Evaluating rules...")
    if isinstance(data, dict) and data.get("amount", 0) > 10000:
        trace.append("Rule triggered: high_value_transaction")
        return "FLAGGED"
    trace.append("No rules triggered")
    return "CLEAR"
