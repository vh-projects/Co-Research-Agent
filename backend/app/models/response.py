from pydantic import BaseModel

from app.models.report import CompanyReport


class ResearchResponse(BaseModel):
    success: bool
    report: CompanyReport | None = None
    error: str | None = None

    