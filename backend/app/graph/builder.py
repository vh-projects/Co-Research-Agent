from langgraph.graph import START, END, StateGraph

from app.nodes.ai_opportunities import ai_opportunities_node
from app.nodes.business import business_node
from app.nodes.ceo_pitch import ceo_pitch_node
from app.nodes.challenges import challenges_node
from app.nodes.evidence import evidence_node
from app.nodes.overview import overview_node
from app.nodes.report import report_node
from app.nodes.research import research_node
from app.nodes.validator import validator_node

from app.state import ResearchState


def route_validation(state: ResearchState):
    if state.get("is_valid_company"):
        return "research"

    return END


builder = StateGraph(ResearchState)


builder.add_node("validator", validator_node)
builder.add_node("research", research_node)
builder.add_node("evidence", evidence_node)

builder.add_node("overview", overview_node)
builder.add_node("business", business_node)
builder.add_node("challenges", challenges_node)
builder.add_node("ai_opportunities", ai_opportunities_node)

builder.add_node("ceo_pitch", ceo_pitch_node)
builder.add_node("report", report_node)


builder.add_edge(START, "validator")


builder.add_conditional_edges(
    "validator",
    route_validation,
    {
        "research": "research",
        END: END,
    },
)


builder.add_edge("research", "evidence")


builder.add_edge("evidence", "overview")
builder.add_edge("evidence", "business")
builder.add_edge("evidence", "challenges")
builder.add_edge("evidence", "ai_opportunities")


builder.add_edge("overview", "ceo_pitch")
builder.add_edge("business", "ceo_pitch")
builder.add_edge("challenges", "ceo_pitch")
builder.add_edge("ai_opportunities", "ceo_pitch")
builder.add_edge("ceo_pitch", "report")
builder.add_edge("report", END)

graph = builder.compile()

