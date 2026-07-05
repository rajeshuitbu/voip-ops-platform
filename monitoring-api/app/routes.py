
from fastapi import APIRouter
from app.service import (
    get_kamailio_status,
    get_kamailio_version,
    get_kamailio_details
)

router = APIRouter()


@router.get("/")
def root():
    return {
        "application": "VoIP Ops Platform",
        "status": "running"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/kamailio/status")
def kamailio_status():
    return get_kamailio_status()


@router.get("/kamailio/version")
def kamailio_version():
    return get_kamailio_version()


@router.get("/kamailio/details")
def kamailio_details():
    return get_kamailio_details()
