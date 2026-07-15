from pydantic import BaseModel, Field


class BusinessAnalysis(BaseModel):
    core_operations: list[str] = Field(default_factory=list)

    revenue_streams: list[str] = Field(default_factory=list)

    customer_segments: list[str] = Field(default_factory=list)

    value_proposition: str = ""

    operational_workflow: list[str] = Field(default_factory=list)

    