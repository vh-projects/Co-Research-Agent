from typing import TypedDict

from app.models.business import BusinessAnalysis
from app.models.challenge import Challenges
from app.models.evidence import Evidence
from app.models.opportunity import AIOpportunities
from app.models.overview import CompanyOverview
from app.models.pitch import CEOPitch
from app.models.report import CompanyReport
from app.models.search import SearchResult


class ResearchState(TypedDict, total=False):
    # User input
    company_name: str

    # Validation
    is_valid_company: bool

    # Research
    search_results: list[SearchResult]

    # Structured outputs
    evidence: Evidence
    overview: CompanyOverview
    business: BusinessAnalysis
    challenges: Challenges
    ai_opportunities: AIOpportunities
    ceo_pitch: CEOPitch

    # Final output
    report: CompanyReport

    # Error handling
    error: str

