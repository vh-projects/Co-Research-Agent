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
    sections = []

    for i, result in enumerate(search_results, start=1):
        sections.append(
            f"""
Source {i}

Title:
{result.title}

Content:
{result.content}
"""
        )

# URL:
# {result.url}
    return "\n\n".join(sections)


def build_evidence_prompt(company_name: str, search_results: list) -> str:
    sources = _format_search_results(search_results)

    return f"""
You are an expert business research analyst.

Your task is to analyze the following public information about the company.

Company:
{company_name}

Public Information:
{sources}

Instructions:

- Use ONLY the information provided.
- Do NOT invent facts.
- If information is unavailable, use an empty string or empty list.
- Do NOT include citations or URLs.
- Return ONLY valid JSON.

Expected JSON:

{EVIDENCE_EXAMPLE}
"""


def build_overview_prompt(evidence: Evidence) -> str:
    
    return f"""
You are an expert business analyst.

Using the structured company evidence below, generate a concise company overview.

Evidence:

{evidence.model_dump_json(indent=2)}

Instructions:

- Do not invent facts.
- Return ONLY valid JSON.

Expected JSON:

{OVERVIEW_EXAMPLE}
"""


def build_business_prompt(evidence: Evidence) -> str:
    
    return f"""
You are a business strategy consultant.

Analyze the company evidence and describe the business model.

Evidence:

{evidence.model_dump_json(indent=2)}

Return ONLY valid JSON.

Expected JSON:

{BUSINESS_EXAMPLE}
"""


def build_challenges_prompt(evidence: Evidence) -> str:
    
    return f"""
You are a management consultant.

Identify the company's biggest business challenges based only on the evidence.

Evidence:

{evidence.model_dump_json(indent=2)}

Return ONLY valid JSON.

Expected JSON:

{CHALLENGES_EXAMPLE}
"""


def build_ai_opportunities_prompt(evidence: Evidence) -> str:
    
    return f"""
You are an AI strategy consultant.

Recommend practical AI opportunities for this company.

Evidence:

{evidence.model_dump_json(indent=2)}

Requirements:

- Prioritize high business value.
- Recommend realistic AI solutions.
- Return ONLY valid JSON.

Expected JSON:

{AI_OPPORTUNITIES_EXAMPLE}
"""


def build_ceo_pitch_prompt(
    evidence: Evidence,
    overview: CompanyOverview,
    business: BusinessAnalysis,
    challenges: Challenges,
    opportunities: AIOpportunities,
) -> str:
    return f"""
You are an AI Strategy Consultant preparing an executive briefing for the CEO.

Your objective is to convince the CEO where AI can create the highest business impact.

Company Evidence

{evidence.model_dump_json(indent=2)}

Company Overview

{overview.model_dump_json(indent=2)}

Business Analysis

{business.model_dump_json(indent=2)}

Business Challenges

{challenges.model_dump_json(indent=2)}

AI Opportunities

{opportunities.model_dump_json(indent=2)}

Instructions:

- Keep the pitch concise.
- Focus on business value rather than technical implementation.
- Prioritize recommendations with the highest ROI.
- Do not introduce information not supported by the provided data.
- Return ONLY valid JSON.

Expected JSON:

{CEO_PITCH_EXAMPLE}
"""
