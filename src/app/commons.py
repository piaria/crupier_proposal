from abc import ABC, abstractmethod
from typing import Dict


class Integration(ABC):
    @abstractmethod
    def create_order_webhook(self, payload: Dict):
        """
        webhook que se invoca desde a tienda para dar aviso de la creacion de una orden.
        La orden se debe cargar en en core
        """
        ...

    @abstractmethod
    def handle_core_order_state_changed(
        client_id: int, store_id: int, order_id: int, new_state: str
    ):
        """cambio el estado en una orden del core y la integracion debe actualizarla"""
        ...

    def activate_store(self, client_id: int, store_id: int):
        """plantilla para activar una tienda"""
        self.save_store(client_id, store_id)
        self.set_pickup_points()
        self.set_shipping_policies()

    @abstractmethod
    def save_store(client_id: int, store_id: int):
        """guarda el store en la integracion"""
        ...

    @abstractmethod
    def set_pickup_points():
        """sincroniza los pickup_points en la tienda"""
        ...

    @abstractmethod
    def set_shipping_policies():
        """sincroniza las shipping_policies en la tienda"""
        ...
