from pydantic import BaseModel
from typing import List


class OrderSchema(BaseModel):
    order_id: int
    user_id: int
    item_ids: List[int]
    total_amount: float
