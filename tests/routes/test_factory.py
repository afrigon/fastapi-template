# -*- coding: utf-8 -*-

from app.routes import RouterFactory


def test_whenCreatingRouter_thenDefaultRouteIsRegistered(app):
    router = RouterFactory().create()
    assert 'default' in router.routes
