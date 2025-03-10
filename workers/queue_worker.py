from database import SessionLocal
from models import OrderModel
import time
from queue import Queue
import threading

order_queue = Queue()
order_status = {}


def process_orders():
    while True:
        if not order_queue.empty():
            order_data = order_queue.get()
            order_status[order_data["order_id"]] = "Processing"
            time.sleep(2)  # Simulated processing time
            order_status[order_data["order_id"]] = "Completed"

            db = SessionLocal()
            order = db.query(OrderModel).filter(OrderModel.order_id == order_data["order_id"]).first()
            if order:
                order.status = "Completed"
                db.commit()
            db.close()


worker_thread = threading.Thread(target=process_orders, daemon=True)
worker_thread.start()
