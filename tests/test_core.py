from operator import truediv
import pytest
from app.core.core import Core
from app.vtex.vtex import VTEX
from tests.commons import MethodCalled

core: Core = Core()


class DummyCrupier:
    def handle_core_order_state_changed(
        self,
        integration: str,
        client_id: int,
        store_id: int,
        order_id: int,
        new_state: str,
    ):
        raise MethodCalled()


def test_order_state_changed_invoiced(monkeypatch: pytest.MonkeyPatch):
    core.crupier_class = DummyCrupier

    try:
        core.order_state_changed(VTEX, 1, 1, 20, "test")
    except MethodCalled:
        ...
    else:
        pytest.fail(
            "Method handle_core_order_state_changed should have been called"
        )
