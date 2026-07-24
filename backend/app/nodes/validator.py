# app/nodes/validator

import re
from app.services.tavily_search import tavily
from app.state import ResearchState


def normalize(text: str) -> str:
    """
    Normalize text for deterministic company matching.
    """
    text = text.lower()

    text = re.sub(
        r"\b(inc|corp|corporation|ltd|limited|llc|plc|company|co)\b",
        "",
        text,
    )

    text = re.sub(r"[^a-z0-9\s]", "", text)

    return " ".join(text.split())


def validator_node(state: ResearchState) -> ResearchState:
    company_name = state["company_name"].strip()

    results = tavily.search(
        query=f'"{company_name}" company',
        max_results=3,
    )

    if not results:
        return {
            "progress": "Company not found.",
            "is_valid_company": False,
            "error": f'Unable to verify "{company_name}".',
        }

    normalized_input = normalize(company_name)

    title = normalize(results[0].title)

    if normalized_input not in title and title not in normalized_input:
        return {
            "progress": "Company validation failed.",
            "is_valid_company": False,
            "error": f'"{company_name}" could not be confidently matched.',
        }

    return {
        "progress": "Company verified.",
        "company_name": company_name,
        "is_valid_company": True,
    }

