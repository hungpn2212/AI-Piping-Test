import logging

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from app.constants import COUNTRY_MAPPINGS, Season, CountryCode
from app.models import RecommendationResponse, RecommendationRequest, ErrorMessage
from app.service import generate_recommendations

app = FastAPI(
    summary="Travel Recommendations API",
    version="0.0.1",
)
logger = logging.getLogger(__name__)


@app.get(
    '/recommendations',
    response_model=RecommendationResponse,
    responses={400: {'model': ErrorMessage}, 500: {'model': ErrorMessage}},
)
async def get_recommendations(
    country: str = Query(..., enum=CountryCode.get_all()),
    season: str = Query(..., enum=Season.get_all()),
) -> RecommendationResponse:
    if season not in Season.get_all():
        return JSONResponse(
            status_code=400,
            content={'message': 'Invalid season'},
        )

    if country not in CountryCode.get_all():
        return JSONResponse(
            status_code=400,
            content={'message': 'Invalid country'},
        )

    country_name = COUNTRY_MAPPINGS[country]
    try:
        recommendations = generate_recommendations(season, country_name)
    except Exception as e:
        logger.error(
            f'Getting this error when calling chatgpt API to get recommendation: {e}')
        return JSONResponse(
            status_code=500,
            content={'message': 'Internal server error'},
        )

    response: RecommendationRequest = RecommendationResponse(
        country=country_name,
        season=season,
        recommendations=recommendations,
    )
    return JSONResponse(
        jsonable_encoder(response),
        status_code=200,
    )
