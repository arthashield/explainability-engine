from app.compliance.rules import evaluate_rules

def run_compliance_checks(data):
    trace = []
    trace.append("Received input for compliance checks")
    result = evaluate_rules(data, trace)
    trace.append(f"Final Result: {result}")
    return trace
