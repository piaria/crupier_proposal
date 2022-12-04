from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class Vtex_Dimention(BaseModel):
    cubicweight: int
    height: int
    length: int
    weight: int
    width: int


class Vtex_AdditionalInfo(BaseModel):
    dimension: Vtex_Dimention


class Vtex_Item(BaseModel):
    productId: int
    quantity: int
    name: str
    additionalInfo: Vtex_AdditionalInfo


class Vtex_Order(BaseModel):
    orderId: str
    status: str
    creationDate: datetime
    items: List[Vtex_Item]
