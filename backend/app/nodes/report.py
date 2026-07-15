from app.models.report import CompanyReport
from app.state import ResearchState


def report_node(state: ResearchState) -> ResearchState:
    
    print("===== REPORT NODE EXECUTED =====")

    report = CompanyReport(
        evidence=state["evidence"],
        overview=state["overview"],
        business=state["business"],
        challenges=state["challenges"],
        ai_opportunities=state["ai_opportunities"],
        ceo_pitch=state["ceo_pitch"],
    )

    print(report)
    return {
        "progress": "Report completed.",
        "report": report,
    }

