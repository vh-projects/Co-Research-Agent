# from pydantic import BaseModel, Field
# from app.models.search import SearchResult


# class NewsItem(BaseModel):
#     title: str
#     summary: str
#     source: str


# class Evidence(BaseModel):
#     company_name: str
#     industry: str = ""
#     headquarters: str = ""
#     geographic_presence: list[str] = Field(default_factory=list)
#     company_size: str = ""
#     employee_count: str = ""
#     founded: str = ""

#     products_services: list[str] = Field(default_factory=list)
#     business_model: str = ""
#     technologies_used: list[str] = Field(default_factory=list)
#     recent_news: list[NewsItem] = Field(default_factory=list)
#     key_observations: list[str] = Field(default_factory=list)

#     # Attached by the application after validation.
#     citations: list[SearchResult] = Field(default_factory=list)





from pydantic import BaseModel, Field
from app.models.search import SearchResult


class NewsItem(BaseModel):
    title: str
    summary: str
    source: str


class Evidence(BaseModel):
    company_name: str
    industry: str | None
    headquarters: str | None
    geographic_presence: list[str]
    company_size: str | None
    employee_count: str | None
    founded: str | None
    products_services: list[str]
    business_model: str | None
    technologies_used: list[str]
    recent_news: list[NewsItem]
    key_observations: list[str]

    # Attached by the application after validation.
    citations: list[SearchResult] = Field(default_factory=list)