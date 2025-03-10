from sqlalchemy.orm import Session
from models import OrderModel
from workers.queue_worker import order_status


def get_metrics(db: Session):
    """Calculates order statistics."""
    total_orders = db.query(OrderModel).count()
    completed_count = db.query(OrderModel).filter(OrderModel.status == "Completed").count()
    pending_count = db.query(OrderModel).filter(OrderModel.status == "Pending").count()
    processing_count = sum(1 for status in order_status.values() if status == "Processing")
    avg_processing_time = 2  # Simulated value for now

    return {
        "total_orders": total_orders,
        "orders_pending": pending_count,
        "orders_processing": processing_count,
        "orders_completed": completed_count,
        "average_processing_time": avg_processing_time
    }
