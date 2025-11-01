def apply_gdpr_rules(data, trace):
    trace.append("[GDPR] Evaluating data privacy obligations...")
    personal_fields = ["email", "phone", "aadhaar"]
    leaked = [field for field in personal_fields if field in data]
    if leaked:
        trace.append(f"[GDPR] Rule Trigger: PII detected: {leaked}")
        return "GDPR_CONCERN"
    return "GDPR_CLEAR"
