from fastapi import APIRouter
from app.service import restart_kamailio

router = APIRouter()


@router.get("/")
def root():
    return {
        "application": "VoIP Self-Healing Engine",
        "status": "running"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/kamailio/restart")
def restart():
    return restart_kamailio()
