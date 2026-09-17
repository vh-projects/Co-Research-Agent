# from pydantic import BaseModel, Field


# class BusinessChallenge(BaseModel):
#     title: str
#     description: str
#     impact: str


# class Challenges(BaseModel):
#     challenges: list[BusinessChallenge] = Field(default_factory=list)





from pydantic import BaseModel


class BusinessChallenge(BaseModel):
    title: str
    description: str
    impact: str


class Challenges(BaseModel):
    challenges: list[BusinessChallenge]