from fastapi import Query
from pydantic import BaseModel, Field


class Suggestion(BaseModel):
    name: str = Field()
    latitude: str = Field()
    longitude: str = Field()
    score: float = Field(ge=0, le=1)


class SuggestionsResponse(BaseModel):
    suggestions: list[Suggestion] = Field()


class SuggestionsParams(BaseModel):
    q: str = Query(description="City name.")
    latitude: str | None = Query(default=None, description="City latitude.")
    longitude: str | None = Query(default=None, description="City longitude.")
