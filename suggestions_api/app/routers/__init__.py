from fastapi import APIRouter
from routers.suggestions import router as suggestions_router


router = APIRouter()
router.include_router(suggestions_router)
