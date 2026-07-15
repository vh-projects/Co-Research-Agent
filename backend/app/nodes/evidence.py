from app.llm.client import llm
from app.llm.prompts import build_evidence_prompt
from app.models.evidence import Evidence
from app.state import ResearchState
from app.utils.json_parser import extract_json


def evidence_node(state: ResearchState) -> ResearchState:
    company_name = state["company_name"]
    search_results = state["search_results"]

    prompt = build_evidence_prompt(
        company_name=company_name,
        search_results=search_results,
    )

    print("=" * 80)
    print(f"Prompt length: {len(prompt):,} characters")
    print("=" * 80)

    print(f"Search Results: {len(search_results)}")
    
    response = llm.invoke(prompt)

    data = extract_json(response)

    evidence = Evidence.model_validate(data)

    # Attach citations deterministically
    evidence.citations = search_results

    return {
        "progress": "Evidence synthesized.",
        "evidence": evidence,
    }

