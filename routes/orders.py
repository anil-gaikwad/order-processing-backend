from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services.order_service import create_order as create_order_service, get_order_status as get_order_status_service
from schema import OrderSchema

order_router = APIRouter(prefix="/api", tags=["Orders"])


@order_router.post("/order")
def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    """API endpoint for creating an order."""
    return create_order_service(order, db)


@order_router.get("/order/{order_id}")
def get_order_status(order_id: int, db: Session = Depends(get_db)):
    """API endpoint for fetching order status."""
    order_status = get_order_status_service(order_id, db)
    if order_status is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_status