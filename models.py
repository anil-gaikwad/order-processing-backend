from sqlalchemy import Column, Integer, Float, String, Text
from database import Base


class OrderModel(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    item_ids = Column(Text, nullable=False)  # Store as comma-separated values
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="Pending")
