from app.llm.prompts import build_challenges_prompt
from app.models.challenge import Challenges
from app.state import ResearchState
from app.utils.llm import generate_structured_output


def challenges_node(state: ResearchState) -> ResearchState:
    challenges = generate_structured_output(
        prompt=build_challenges_prompt(state["evidence"]),
        model=Challenges,
    )

    return {
        "progress": "Identifying business challenges...",
        "challenges": challenges,
    }

