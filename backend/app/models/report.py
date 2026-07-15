from pydantic import BaseModel

from app.models.business import BusinessAnalysis
from app.models.challenge import Challenges
from app.models.evidence import Evidence
from app.models.opportunity import AIOpportunities
from app.models.overview import CompanyOverview
from app.models.pitch import CEOPitch


class CompanyReport(BaseModel):
    evidence: Evidence

    overview: CompanyOverview

    business: BusinessAnalysis

    challenges: Challenges

    ai_opportunities: AIOpportunities

    ceo_pitch: CEOPitch

