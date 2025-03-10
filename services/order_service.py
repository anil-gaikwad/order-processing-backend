from sqlalchemy.orm import Session
from models import OrderModel
from workers.queue_worker import order_queue, order_status
from schema import OrderSchema


def create_order(order: OrderSchema, db: Session):
    """Handles the creation of a new order."""
    new_order = OrderModel(
        order_id=order.order_id,
        user_id=order.user_id,
        item_ids=",".join(map(str, order.item_ids)),
        total_amount=order.total_amount,
        status="Pending"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    order_status[order.order_id] = "Pending"
    order_queue.put(order.dict())  # Add order to queue for processing

    return {"message": "Order received", "order_id": order.order_id}


def get_order_status(order_id: int, db: Session):
    """Fetches the status of a given order."""
    order = db.query(OrderModel).filter(OrderModel.order_id == order_id).first()
    if not order:
        return None  # Handle missing order at the route level
    return {"order_id": order.order_id, "status": order.status}
