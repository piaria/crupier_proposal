from typing import Dict
from app.utils import new
from app.core.core import Core
from app.core.models import Core_Order


class Crupier:
    core_class = Core
    integration_classes: Dict[str, str] = {
        "vtex": "app.vtex.vtex.VtexIntegration"
    }

    def handle_core_order_state_changed(
        self,
        integration_name: str,
        client_id: int,
        store_id: int,
        order_id: int,
        new_state: str,
    ):
        integration_class = self.integration_classes[integration_name]
        new(integration_class).handle_core_order_state_changed(
            client_id, store_id, order_id, new_state
        )

    def create_order(self, order: Core_Order):
        return self.core_class().create_order(order)

    def activate_store(
        self, integration_name: str, client_id: int, store_id: int
    ):
        integration_class = self.integration_classes[integration_name]
        new(integration_class).activate_store(client_id, store_id)

    def get_pickup_points():
        return new(Core).get_pickup_points()

    def get_shipping_policies():
        return new(Core).get_shipping_policies()
