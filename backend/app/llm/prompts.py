# app/llm/prompts

from app.llm.examples import (
    BUSINESS_EXAMPLE,
    CEO_PITCH_EXAMPLE,
    CHALLENGES_EXAMPLE,
    EVIDENCE_EXAMPLE,
    OVERVIEW_EXAMPLE,
    AI_OPPORTUNITIES_EXAMPLE,
)
from app.models.evidence import Evidence
from app.models.business import BusinessAnalysis
from app.models.challenge import Challenges
from app.models.opportunity import AIOpportunities
from app.models.overview import CompanyOverview


def _format_search_results(search_results):
    return "\n\n".join(
        f"[{i}] {result.title}\n{result.content.strip()}"
        for i, result in enumerate(search_results, 1)
    )


def build_evidence_prompt(company_name: str, search_results: list) -> str:
    sources = _format_search_results(search_results)

    return f"""
Extract company information.

Company: {company_name}

Sources:
{sources}

Use only the sources.
Missing values: "" or [].
Exclude citations/URLs.
Output JSON only.

Example:
{EVIDENCE_EXAMPLE}
"""


def build_overview_prompt(evidence: Evidence) -> str:
    return f"""
Generate a company overview.

Evidence:
{evidence.model_dump_json()}

Output JSON only.

Example:
{OVERVIEW_EXAMPLE}
"""


def build_business_prompt(evidence: Evidence, overview: CompanyOverview,) -> str:
    return f"""
Analyze the company's business model.

Overview:
{overview.model_dump_json()}

Evidence:
{evidence.model_dump_json(
    include={
        "products_services",
        "business_model",
        "technologies_used",
        "key_observations",
    }
)}

Output JSON only.

Example:
{BUSINESS_EXAMPLE}
"""


def build_challenges_prompt(business: BusinessAnalysis,) -> str:
    return f"""
Identify the company's business challenges.

Business:
{business.model_dump_json()}

Output JSON only.

Example:
{CHALLENGES_EXAMPLE}
"""


def build_ai_opportunities_prompt(business: BusinessAnalysis, challenges: Challenges,) -> str:
    return f"""
Recommend practical AI opportunities.

Business:
{business.model_dump_json()}

Challenges:
{challenges.model_dump_json()}

Prioritize high business value.
Output JSON only.

Example:
{AI_OPPORTUNITIES_EXAMPLE}
"""


def build_ceo_pitch_prompt(
    overview: CompanyOverview, business: BusinessAnalysis,
    challenges: Challenges, opportunities: AIOpportunities,
) -> str:
    return f"""
Prepare an executive AI recommendation.

Overview:
{overview.model_dump_json()}

Business:
{business.model_dump_json()}

Challenges:
{challenges.model_dump_json()}

AI Opportunities:
{opportunities.model_dump_json()}

Focus on business value and ROI.
Output JSON only.

Example:
{CEO_PITCH_EXAMPLE}
"""

