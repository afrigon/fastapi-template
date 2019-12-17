# -*- coding: utf-8 -*-

from unittest.mock import MagicMock
from app.routes import Router


def create_route():
    route = MagicMock()
    route.register = MagicMock()

    return route


ROUTE_A = create_route()
ROUTE_B = create_route()


def test_whenRegisteringRoutes_thenRoutesAreRegistered(app):
    router = Router(ROUTE_A, ROUTE_B)
    router.register(app)

    ROUTE_A.register.assert_called_once_with(app)
    ROUTE_B.register.assert_called_once_with(app)
