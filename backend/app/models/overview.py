from pydantic import BaseModel, ConfigDict,  Field


class CompanyOverview(BaseModel):
    # summary: str
    # mission: str = ""
    # vision: str = ""
    # target_market: list[str] = Field(default_factory=list)
    # competitive_position: str = ""
    # strengths: list[str] = Field(default_factory=list)


    model_config = ConfigDict(extra="forbid")

    summary: str
    mission: str
    vision: str
    target_market: list[str]
    competitive_position: str
    strengths: list[str]    