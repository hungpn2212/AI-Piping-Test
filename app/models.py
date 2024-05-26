from pydantic import BaseModel
from app.constants import Season, Country, CountryCode


class ErrorMessage(BaseModel):
    message: str


class RecommendationRequest(BaseModel):
    country: CountryCode # type: ignore
    season: Season


class RecommendationResponse(BaseModel):
    country: Country
    season: Season
    recommendations: list[str]
