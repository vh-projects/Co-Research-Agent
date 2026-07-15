from pydantic import BaseModel, Field


class CEOPitch(BaseModel):
    executive_summary: str

    recommended_first_step: str

    recommended_ai_initiatives: list[str] = Field(default_factory=list)

    expected_business_impact: list[str] = Field(default_factory=list)


    closing_statement: str