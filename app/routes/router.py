# -*- coding: utf-8 -*-

from .route import Route


class Router:
    def __init__(self, *routes: [Route]):
        self.routes = routes

    def register(self, app):
        for route in self.routes:
            route.register(app)
