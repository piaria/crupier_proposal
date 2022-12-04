from app.core.models import Core_Order
from app.utils import new


class Core:
    crupier_class = "app.crupier.Crupier"

    def create_order(self, order: Core_Order):
        return order

    def order_state_changed(
        self,
        integration: str,
        client_id: int,
        store_id: int,
        order_id: int,
        new_state: str,
    ):
        # cambió el estado de una orden en el core y se avisa a la integracion

        new(self.crupier_class).handle_core_order_state_changed(
            integration, client_id, store_id, order_id, new_state
        )

    def get_pickup_points():
        return []

    def get_shipping_policies():
        return []
