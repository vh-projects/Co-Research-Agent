from app.llm.prompts import build_overview_prompt
from app.models.overview import CompanyOverview
from app.state import ResearchState
from app.utils.llm import generate_structured_output


def overview_node(state: ResearchState) -> ResearchState:
    overview = generate_structured_output(
        prompt=build_overview_prompt(state["evidence"]),
        model=CompanyOverview,
    )

    return {
        "progress": "Generating company overview...",
        "overview": overview,
    }

