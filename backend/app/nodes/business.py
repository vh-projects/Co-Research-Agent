from app.llm.prompts import build_business_prompt
from app.models.business import BusinessAnalysis
from app.state import ResearchState
from app.utils.llm import generate_structured_output


def business_node(state: ResearchState) -> ResearchState:
    business = generate_structured_output(
        prompt=build_business_prompt(state["evidence"]),
        model=BusinessAnalysis,
    )

    return {
        "progress": "Analyzing business model...",
        "business": business,
    }

