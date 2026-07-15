from app.llm.prompts import build_ceo_pitch_prompt
from app.models.pitch import CEOPitch
from app.state import ResearchState
from app.utils.llm import generate_structured_output


def ceo_pitch_node(state: ResearchState) -> ResearchState:
    pitch = generate_structured_output(
        prompt=build_ceo_pitch_prompt(
            evidence=state["evidence"],
            overview=state["overview"],
            business=state["business"],
            challenges=state["challenges"],
            opportunities=state["ai_opportunities"],
        ),
        model=CEOPitch,
    )

    return {
        "progress": "Preparing executive pitch...",
        "ceo_pitch": pitch,
    }

