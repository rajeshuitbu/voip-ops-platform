from fastapi import APIRouter

from app.service import check_options
from app.stats import get_statistics

router = APIRouter()


@router.get("/")
def root():

    return {
        "application": "VoIP OPTIONS Monitor",
        "status": "running"
    }


@router.get("/health")
def health():

    return {
        "status": "healthy"
    }


@router.get("/options/status")
def options_status():

    return check_options()


@router.post("/options/check")
def options_check():

    return check_options()


@router.get("/options/statistics")
def statistics():

    return get_statistics()
