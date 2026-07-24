# app/nodes/report

from app.models.report import CompanyReport
from app.state import ResearchState


def report_node(state: ResearchState) -> ResearchState:
    
    report = CompanyReport(
        evidence=state["evidence"],
        overview=state["overview"],
        business=state["business"],
        challenges=state["challenges"],
        ai_opportunities=state["ai_opportunities"],
        ceo_pitch=state["ceo_pitch"],
    )


    return {
        "progress": "Report completed.",
        "report": report,
    }

