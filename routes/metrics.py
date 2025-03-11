from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.metrics_service import get_metrics as get_metrics_service

metric_router = APIRouter(prefix="/api", tags=["Metrics"])


@metric_router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    """API endpoint for fetching order metrics."""
    return get_metrics_service(db)
