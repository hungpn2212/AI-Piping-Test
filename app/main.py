import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.constants import COUNTRY_MAPPINGS, Season
from app.service import generate_recommendations

app = FastAPI()
logger = logging.getLogger(__name__)


@app.get('/recommendations')
async def main(country: str, season: str):
    if season not in Season.get_all_seasons():
        return JSONResponse(
            status_code=400,
            content={'message': 'Invalid season'},
        )

    if country.upper() not in COUNTRY_MAPPINGS:
        return JSONResponse(
            status_code=400,
            content={'message': 'Invalid country'},
        )

    country_name = COUNTRY_MAPPINGS[country.upper()]
    try:
        recommendations = generate_recommendations(season, country_name)
        return {'country': country_name, 'season': season, 'recommendations': recommendations}
    except Exception as e:
        logger.error(
            f'Getting this error when calling chatgpt API to get recommendation: {e}')
        return JSONResponse(
            status_code=500,
            content={'message': 'Internal server error'},
        )
