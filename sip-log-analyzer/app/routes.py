from fastapi import APIRouter
from app.service import analyze_log

router = APIRouter()


@router.get("/")
def root():
    return {
        "application": "VoIP SIP Log Analyzer",
        "status": "running"
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/analyze")
def analyze():
    return analyze_log()
