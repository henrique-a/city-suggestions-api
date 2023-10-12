from fastapi import APIRouter, Depends
from models.suggestions import Suggestion, SuggestionsResponse, SuggestionsParams
from db.services import CityService
from config import CANADA_FIPS_CODE, COUNTRY_NAME


router = APIRouter(prefix="/suggestions", tags=["suggestions"])


@router.get("/", response_model=SuggestionsResponse)
async def suggestions(params: SuggestionsParams = Depends()):
    city_service = CityService()
    suggestions = city_service.get_suggestions(params.q, params.latitude, params.longitude)
    suggestions_response = []
    for suggestion in suggestions:
        state = suggestion["state"] if suggestion["country"] == "US" else CANADA_FIPS_CODE[suggestion["state"]]
        country = COUNTRY_NAME[suggestion["country"]]
        suggestion_response = Suggestion(
            name=f"{suggestion['name']}, {state}, {country}",
            latitude=str(suggestion["location"]["lat"]),
            longitude=str(suggestion["location"]["lon"]),
            score=suggestion["score"],
        )
        suggestions_response.append(suggestion_response)
    return SuggestionsResponse(suggestions=suggestions_response).model_dump()
