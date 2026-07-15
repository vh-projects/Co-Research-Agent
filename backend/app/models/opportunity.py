from pydantic import BaseModel, Field


class AIOpportunity(BaseModel):
    title: str

    description: str

    business_value: str

    implementation_complexity: str

    priority: str


class AIOpportunities(BaseModel):
    opportunities: list[AIOpportunity] = Field(default_factory=list)

