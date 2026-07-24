# app/nodes/ai_opportunities
from app.llm.prompts import build_ai_opportunities_prompt
from app.models.opportunity import AIOpportunities
from app.state import ResearchState
from app.utils.llm import generate_structured_output

def ai_opportunities_node(state: ResearchState) -> ResearchState:
    opportunities = generate_structured_output(
        prompt=build_ai_opportunities_prompt(state["business"], state["challenges"]),
        model=AIOpportunities,
    )

    return {
        "progress": "Generating AI opportunities...",
        "ai_opportunities": opportunities,
    }

