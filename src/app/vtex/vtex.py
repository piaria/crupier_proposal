from abc import ABC, abstractmethod
from typing import Dict

from app.core.models import Core_Dimention, Core_Order, Core_OrderItem
from app.vtex.models import Vtex_Dimention, Vtex_Item, Vtex_Order
from app.crupier import Crupier
from app.commons import Integration
from app.utils import new

VTEX = "vtex"


class VtexIntegration(Integration):
    crupier_class = Crupier

    def create_order_webhook(self, payload: Dict):
        vtex_order = Vtex_Order.parse_obj(payload)
        order = self._transform_order(vtex_order)
        return new(self.crupier_class).create_order(order)

    def handle_core_order_state_changed(
        client_id: int, store_id: int, order_id: int, new_state: str
    ):
        ...
    

    def save_store(client_id: int, store_id: int):
        """guarda el store en la integracion"""
        ...

    def set_pickup_points():
        """sincroniza los pickup_points en la tienda"""
        ...

    def set_shipping_policies():
        """sincroniza las shipping_policies en la tienda"""
        ...

    def _transform_order(self, order: Vtex_Order):
        items = [self._transform_order_item(item) for item in order.items]
        return Core_Order(
            store_order_id=order.orderId, items=items, source=VTEX
        )

    def _transform_order_item(self, item: Vtex_Item):
        return Core_OrderItem(
            name=item.name,
            product_id=item.productId,
            quantity=item.quantity,
            dimention=self._transform_order_item_dimention(
                item.additionalInfo.dimension
            ),
        )

    def _transform_order_item_dimention(self, dimention: Vtex_Dimention):
        return Core_Dimention(
            cubicweight=dimention.cubicweight,
            height=dimention.height,
            weight=dimention.weight,
            width=dimention.width,
            length=dimention.length,
        )
