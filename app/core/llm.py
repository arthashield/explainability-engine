import os
from typing import List

def _fallback_justifier(trace: List[str]) -> str:
    # Simple deterministic summarizer if no LLM key configured
    lines = []
    lines.append("Explainability summary:")
    for step in trace:
        s = str(step).strip()
        if s:
            lines.append(s if len(s) < 200 else s[:197] + "...")
    return " ".join(lines)

def generate_justification(trace: List[str]) -> str:
    # If OPENAI_API_KEY is present, use OpenAI chat completion.
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        try:
            import openai
            openai.api_key = api_key
            system = "You are an explainability assistant. Produce a concise, auditor-friendly natural language justification for why the system made the decisions in the provided trace. Keep it factual and reference specific steps when helpful."
            user = "Trace steps:\n" + "\n".join([str(x) for x in trace])
            resp = openai.ChatCompletion.create(
                model=os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo'),
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ],
                max_tokens=512,
                temperature=0.0
            )
            answer = resp['choices'][0]['message']['content'].strip()
            return answer
        except Exception as e:
            return _fallback_justifier(trace) + f" (LLM fallback due to error: {e})"
    else:
        return _fallback_justifier(trace) + " (LLM not configured; using deterministic fallback)"

def run_llm_prompt(prompt: str):
    return f"LLM response to: {prompt}"
