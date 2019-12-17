# -*- coding: utf-8 -*-

from . import Router
from .default_route import DefaultRoute
from ..services import DefaultService


class RouterFactory:
    def create(self):
        default = DefaultRoute(DefaultService())

        return Router(default)
