# -*- coding: utf-8 -*-

from .route import Route


class DefaultRoute(Route):
    def __init__(self, service):
        self.service = service

    def get_name(self):
        return 'default'

    def register(self, app):
        app.add_api_route('/',
                          self.get,
                          methods=['GET'],
                          name='root',
                          tags=['Default'])

    def get(self):
        return self.service.get()
