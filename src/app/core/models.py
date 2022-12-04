from datetime import datetime
from typing import List
import uuid

from pydantic import BaseModel, Field


class Core_Dimention(BaseModel):
    cubicweight: int
    height: int
    length: int
    weight: int
    width: int


class Core_OrderItem(BaseModel):
    name: str
    quantity: int
    product_id: int
    dimention: Core_Dimention


class Core_Order(BaseModel):
    id: str = str(uuid.uuid1())
    creation: datetime = datetime.now()
    source: str
    store_order_id: str = None
    store_id: int = None
    items: List[Core_OrderItem] = []
