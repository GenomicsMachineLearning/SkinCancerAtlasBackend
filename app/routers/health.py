from fastapi import APIRouter
from app.models import HealthResponse
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        version="1.0.0"
    )

@router.get("/ready")
async def readiness_check():
    # Add any readiness checks here (DB connections, etc.)
    return {"status": "ready"}